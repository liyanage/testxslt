//
//  ParameterSet.m
//  TestXSLT
//
//  Created by Marc Liyanage on Sat Mar 09 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import "ParameterSet.h"


@implementation ParameterSet

- (id)init {

	if (self = [super init]) {
		parameters = [[NSMutableArray alloc] init];
		cArray = NULL;
	}

	//	NSLog(@"ParameterSet init, %@", parameters);

	return self;

}

- (void)dealloc {

	[parameters release];
	if (cArray != NULL) {
		free(cArray);
	}

	[super dealloc];
//	NSLog(@"ParameterSet dealloc");
}


- (void)encodeWithCoder:(NSCoder *)coder {
	[coder encodeObject:parameters];
}


- (id)initWithCoder:(NSCoder *)coder {

	if (self = [super init]) {
		[self setParameterSet:[coder decodeObject]];
	}
	return self;

}

- (void)setParameterSet:(NSMutableArray *)array {

	[array retain];
	[parameters release];
	parameters = array;

}


- (void)addParameter:(NSString *)name withValue:(NSString *)value {
	
	NSMutableDictionary *entry = [NSMutableDictionary dictionaryWithCapacity:2];
	[entry setObject:name forKey:@"parameterName"];
	[entry setObject:value forKey:@"parameterValue"];

//	NSLog("entry: %@", entry);	
	
	[parameters addObject:entry];

}



- (void)setField:(NSString *)fieldName atIndex:(int)index toString:(NSString *)s {
	[[parameters objectAtIndex:index] setObject:s forKey:fieldName];
}

- (NSString *)getField:(NSString *)fieldName atIndex:(int)index {
	return [[parameters objectAtIndex:index] objectForKey:fieldName];
}



- (void)removeParameterAtIndex:(int)index {
	[parameters removeObjectAtIndex:index];
}

- (void)removeParameterByName:(NSString *)name {

	int i;
	NSString *currentName;
	
	for (i = 0; i < [self count]; i++) {
		currentName = [self getField:@"parameterName" atIndex:i];
		if ([currentName isEqualToString:name]) {
			[self removeParameterAtIndex:i];
			[self removeParameterByName:name];
		}
	}

}


- (int)count {
	return [parameters count];
}

- (const char **)cArray {

	int i;
	const char **temp;
	
	if (cArray != NULL) {
		free(cArray);
	}

	temp = cArray = malloc((([self count] * 2) + 1) * sizeof(char *));


	for (i = 0; i < [self count]; i++) {

		*(temp++) = (char *)[[self getField:@"parameterName" atIndex:i] cString];
		*(temp++) = (char *)[[self getField:@"parameterValue" atIndex:i] cString];
	
	}
	
	*(temp) = NULL;
	
	return cArray;
}



@end
