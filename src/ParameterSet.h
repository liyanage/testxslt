//
//  ParameterSet.h
//  TestXSLT
//
//  Created by Marc Liyanage on Sat Mar 09 2002.
//  Copyright (c) 2001 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ParameterSet : NSObject <NSCoding> {
	NSMutableArray *parameters;
	const char **cArray;
}

- (void)addParameter:(NSString *)name withValue:(NSString *)value;
- (void)setField:(NSString *)fieldName atIndex:(int)index toString:(NSString *)s;
- (NSString *)getField:(NSString *)fieldName atIndex:(int)index;
- (void)removeParameterAtIndex:(int)index;
- (void)setParameterSet:(NSMutableArray *)array;
- (void)removeParameterByName:(NSString *)name;

- (const char **)cArray;

- (int)count;





@end
