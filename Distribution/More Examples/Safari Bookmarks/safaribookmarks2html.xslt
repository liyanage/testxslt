<?xml version='1.0' encoding='iso-8859-1'?>

<xsl:stylesheet version='1.0' xmlns:xsl='http://www.w3.org/1999/XSL/Transform'>

<xsl:output method='html' version='1.0' encoding='iso-8859-1' indent='no'/>

<!-- An XSLT style sheet to convert a Safari bookmarks list to HTML -->
<!-- You can find your Safari bookmarks file in your home directory under
     Library / Safari / Bookmarks.plist -->
     
<!-- Written by Marc Liyanage (http://www.entropy.ch) -->



<!-- Match toplevel element, emit basic HTML document structure -->

<xsl:template match="plist">

<html>

	<head>
	
		<title>Safari Bookmarks</title>
	
		<style type="text/css">
			.category	
			{
				border-color: #333333;
				border-style: solid;
				border-width: 1px;
				margin: 10px 4px 4px 10px;
				background-color: #cccccc;
			}
			.indent { margin-left: 10px; }
			.categorytitle	
			{
				font-family: Georgia;
				font-size: 16px;
				font-weight: bold;
				font-style: italic;
				color: white;
				background-color: #333333;
				padding: 1px;
			}
			.link	
			{
				font-family: Georgia;
				font-size: 14px;
				font-weight: normal;
				margin: 2px 2px 2px 10px;
			}
			a { text-decoration: none; }
			a:hover { text-decoration: underline; }
		</style>
	
	</head>

	<body>
		<!-- recursively create the body content -->
		<xsl:apply-templates/>
	</body>

</html>

</xsl:template>





<!-- This generic template matches dict entries which act as containers for other items -->
<xsl:template match="dict">

	<xsl:variable name="title" select="string[preceding-sibling::key[text() = 'Title']]"/>

	<div class="category">
		<xsl:if test="$title"><div class="categorytitle"><xsl:value-of select="$title"/></div></xsl:if>
		<xsl:apply-templates select="array"/>
	</div>
	
</xsl:template>


<!-- This more specific template matches dict entries which contain a particular link. Because
     it is more specific it will have precedence over the one above. -->
<xsl:template match="dict[key[text() = 'URIDictionary']]">

		<div class="link"><a href="{string[preceding-sibling::key[text() = 'URLString']]}"><xsl:value-of select="dict[preceding-sibling::key[text() = 'URIDictionary']]/string[preceding-sibling::key[text() = 'title']]"/></a></div>

</xsl:template>



</xsl:stylesheet>