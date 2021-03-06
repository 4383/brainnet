#pragma once

#include <string>
#include <iostream>
#include <math.h>
#include <vector>
#include <list>

using std::max;
using std::min;
using std::cout;
using std::endl;
using std::string;
using std::to_string;
using std::vector;
using std::list;

//#include "msclStringFuncs.h"
//#include "IdentifierTable.h"
//#include "ElementData.h"
//#include "ElementList.h"

class Element;

class Parser
{
    public:
        Parser();
        ~Parser() {cleanUp();}
        void setInFileName(std::string in) {inFileName=in;}
        void setSource(std::string in) {inSource=in;}
        string getCpp() {return outCpp;}
        void resolveProgram(bool printExtraOutput);
        string resolveProgram(string input, string fileIn, bool printExtraOutput=true)
        {
            setSource(input);
            setInFileName(fileIn);
            resolveProgram(printExtraOutput);
            return getCpp();
        }

    private:
        
        void cleanUp();
        void populateCharVectors();
        void initialProgramPopulation();
        ElementData::Type getElementType(char c, ElementData::Type previousType);
        Element * makeElement(ElementData data);
        
    private:
        
        ElementList program={ElementData("", "UNKNOWN_FILE", 0, ElementData::SCOPE)};
        
        string inFileName;
        string inSource;
        string outCpp;
        
        vector<char> whitespaceChars, letterChars, digitChars, operatorChars;
};
