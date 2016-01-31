#!/usr/bin/env python

'''
=> Program to Implement the Simple Text Editor Problem in HackerRank : https://www.hackerrank.com/challenges/simple-text-editor

In this problem, your task is to implement a simple text editor. Initially, a file contains an empty string S. 
Your task is to perform Q operations consisting of the following 4 types:

   1. append(W) - Appends the string W at the end of S.
   2. erase(k) - Erase the last k character of S.
   3. get(k) - Returns the kth character of S.
   4. undo() - Undo the last not previously undone operation of type 1 or 2, so it reverts S to the state before that operation.

'''

initstr = ''		## Initial String
bkpstr = []		## List to store all the Modified values of String

def getInput():
	"Function to parse the user Input"

	nops = input(" ")	## Number of Lines in Input
	ops = []		## List to store the Inputs

	while ( nops > 0 ):		## Taking up the User Inputs and storing in List
		inp = raw_input(" ")
		ops.append(inp)
		nops -= 1
	
	return ops

def parseInput(arr):
	"Function to parse each of the inputs and act accordingly"
	
	for opn in arr :
		if int(opn.split(" ")[0]) == 1:
			appendStr(opn.split(" ")[1])
		elif int(opn.split(" ")[0]) == 2:
			eraseStr(opn.split(" ")[1])
		elif int(opn.split(" ")[0]) == 3:
			print getStr(opn.split(" ")[1])
		elif int(opn.split(" ")[0]) == 4:
			undoStr()
		else :
			print "\n Invalid Input !!"
	
def appendStr(app):
	"Function to Append the string passed as argument with actual String"

	global initstr 
	global bkpstr

	bkpstr.append(initstr)
	initstr += app

def eraseStr(num):
	"Function to erase the last k-characters passed as argument from actual String"

	global initstr
	global bkpstr

	bkpstr.append(initstr)
	initstr = initstr[:-int(num)]

def getStr(num):
	"Function to return the k-th character passed as argument from actual String"

	global initstr
	return initstr[int(num) - 1]

def undoStr():
	"Function to revert the last action performed on the actual String"

	global initstr
	global bkpstr

	initstr = bkpstr.pop()
tr


# Function Calls
ops = getInput()
parseInput(ops)
		
		
		
