<?xml version="1.0" encoding="UTF-8"?>
<!-- $Id$ -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format">
<!-- Need to instruct the XSLT processor to use XML output rules.
     See http://www.w3.org/TR/xslt#output for more details
-->
	<xsl:output method="xml" indent="yes" encoding="UTF-8" />
	<xsl:param name="version" />



	<!-- This template matches the root element of the readme document and emits the page
         master definitions -->
	<xsl:template match='readme'>

		<fo:root>



			<!-- We are producing A4 pages -->
			<fo:layout-master-set>
				<fo:simple-page-master
					master-name="main-a4"
					page-height="297mm" page-width="210mm"
					margin-top="20mm" margin-right="30mm" margin-bottom="10mm" margin-left="20mm"
				>
					<fo:region-before extent="20mm"/>
					<fo:region-body margin-top="0mm" margin-bottom="20mm"/>
					<fo:region-after extent="10mm"/>
				</fo:simple-page-master>

				<fo:page-sequence-master master-name="sequence">
					<fo:single-page-master-reference master-reference="main-a4"/>
				</fo:page-sequence-master>
				
			</fo:layout-master-set>


			<!-- define a master page sequence. Our sequence is simple and only has
			     one kind of page for the entire document. -->
			<fo:page-sequence master-reference="main-a4">

				
				<!-- This fo:static-content element which we are putting into the "after" section
				     will create a small footer with the document title and the page number at the
				     bottom of each page -->
				<fo:static-content flow-name="xsl-region-after">
				<fo:block font-family="Helvetica" font-style="italic" font-size="9pt" margin-top="10mm" color="#fff" background-color="#000" padding="1mm"><xsl:value-of select="/readme/title"/> v<xsl:value-of select="$version"/> – Page <fo:page-number/></fo:block>
				</fo:static-content>
	


				<!-- This is the main and only flow which produces
				     content for the pages -->
				<fo:flow flow-name="xsl-region-body">
				<xsl:apply-templates/>
				<fo:block padding-top="40mm"><fo:external-graphic src="file:///Users/liyanage/cvs/entropy/TestXSLT/TestXSLT-Icon.png"/></fo:block>
				</fo:flow>

			</fo:page-sequence>

		</fo:root>

	</xsl:template>








	<!-- Following are all templates which produce XSL-FO layout elements,
	     usually this means fo:block elements with various attributes -->


	<!-- The title is in a gray box -->
	<xsl:template match='title'>
		<fo:block border="0.5pt" padding-top="2mm" padding-bottom="0mm" padding-left="2mm" background-color="#eeeeee" border-color="#aaaaaa" border-style="solid" margin-top="10mm" margin-left="0mm" font-size="24pt" font-family="Helvetica"  font-weight="bold" line-height="30pt">
			<xsl:apply-templates/> v<xsl:value-of select="$version"/>
		</fo:block>
	</xsl:template>







	<!-- description, requirements and history all look the same because they
	     are all introduce a top-level section -->
	<xsl:template match='description'>
		<fo:block padding-top="8mm" font-family="Helvetica"  font-weight="bold" font-size="18pt">Description</fo:block>

		<xsl:call-template name="sectionrule"/>
		<fo:block margin-left="15mm"><xsl:apply-templates/></fo:block>

	</xsl:template>


	<xsl:template match='requirements'>
		<fo:block padding-top="8mm" font-family="Helvetica"  font-weight="bold" font-size="18pt">Requirements</fo:block>

		<xsl:call-template name="sectionrule"/>
		<fo:block margin-left="15mm"><xsl:call-template name="para"/></fo:block>

	</xsl:template>


	<xsl:template match='history'>
		<fo:block padding-top="8mm" font-family="Helvetica"  font-weight="bold" font-size="18pt">History</fo:block>

		<xsl:call-template name="sectionrule"/>
		<xsl:apply-templates/>
	</xsl:template>







	<!-- This produces a list-block item for history entries -->
	<xsl:template match='entry'>
		<fo:block keep-with-next="always" padding-top="8mm" font-family="Helvetica" font-weight="bold" font-style="italic" font-size="11pt">Version <xsl:value-of select="version"/>, released <xsl:value-of select="date"/></fo:block>

		<xsl:call-template name="entryrule"/>
		<fo:list-block margin-left="15mm"><xsl:apply-templates select="item"/></fo:list-block>
	</xsl:template>


	<xsl:template match='item'>

		<fo:list-item font-size="12pt" line-height="15pt">
			<fo:list-item-label><fo:block padding-top="0.5mm" font-family="ZapfDingbats">&#x2794;</fo:block></fo:list-item-label>
			<fo:list-item-body start-indent="body-start() - 3mm"><fo:block padding-top="0.5mm" font-family="Times"><xsl:apply-templates/></fo:block></fo:list-item-body>
		</fo:list-item>
	</xsl:template>




	<!-- A 1pt-wide horizontal rule for the section headings -->
	<xsl:template name='sectionrule'>
		<fo:block padding-top="-3mm"><fo:leader leader-length="100%" leader-pattern="rule" rule-style="solid" rule-thickness="1pt" color="black"/></fo:block>
	</xsl:template>


	<!-- A 1pw-wide dotted horizontal rule for history entry subheadings -->
	<xsl:template name='entryrule'>
		<fo:block keep-with-next="always" padding-top="-3mm"><fo:leader leader-length="100%" leader-pattern="rule" rule-style="dotted" rule-thickness="1pt"/></fo:block>
	</xsl:template>


	<!-- Our regular paragraphs in the description section -->
	<xsl:template match='para' name='para'>
		<fo:block padding-top="2mm" font-size="12pt" font-family="Times" line-height="15pt"><xsl:apply-templates/></fo:block>

	</xsl:template>


	<!-- Make real, clickable URLs out of url elements -->
	<xsl:template match='url'>
<fo:basic-link external-destination="{.}"><fo:inline color="blue"><xsl:apply-templates/></fo:inline></fo:basic-link>	</xsl:template>


	<!-- The same for email, put make them mailto: URLs -->
	<xsl:template match='email'>

		<fo:basic-link external-destination="mailto:{.}?subject=TestXSLT-Readme-PDF"><fo:inline color="blue"><xsl:apply-templates/></fo:inline></fo:basic-link>
	</xsl:template>


	<!-- Document authorship information -->
	<xsl:template match='author'>

		<fo:block padding-top="5mm" font-size="12pt" font-family="Times" font-weight="bold" font-style="italic"><xsl:apply-templates/></fo:block>

	</xsl:template>




	<!-- The templates above should catch all content, we do not want
	     anything to fall through. If something still does, we will paint
	     a red border around it here so it stands out and we can fix the problem -->
	<xsl:template match='*'>
		<fo:block border-style="solid" border-color="red" border-width="0.5pt" margin-top="10mm" font-size="10pt" font-family="Helvetica" line-height="12pt">
		<xsl:apply-templates/>
		</fo:block>
	</xsl:template>


</xsl:stylesheet>
