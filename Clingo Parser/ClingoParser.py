# Generated from PW-explorer/Clingo Parser/Clingo.g4 by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\20^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32")
        buf.write(u"\n\2\f\2\16\2\35\13\2\3\2\5\2 \n\2\3\2\3\2\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\6\b<\n\b\r\b\16\b")
        buf.write(u"=\3\t\6\tA\n\t\r\t\16\tB\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\7\13P\n\13\f\13\16\13S\13\13\3\f")
        buf.write(u"\3\f\7\fW\n\f\f\f\16\fZ\13\f\3\f\3\f\3\f\2\2\r\2\4\6")
        buf.write(u"\b\n\f\16\20\22\24\26\2\3\5\2\4\4\b\t\17\17\2X\2\33\3")
        buf.write(u"\2\2\2\4#\3\2\2\2\6*\3\2\2\2\b.\3\2\2\2\n\62\3\2\2\2")
        buf.write(u"\f\66\3\2\2\2\16;\3\2\2\2\20@\3\2\2\2\22D\3\2\2\2\24")
        buf.write(u"Q\3\2\2\2\26X\3\2\2\2\30\32\5\22\n\2\31\30\3\2\2\2\32")
        buf.write(u"\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\37\3\2\2\2")
        buf.write(u"\35\33\3\2\2\2\36 \7\16\2\2\37\36\3\2\2\2\37 \3\2\2\2")
        buf.write(u" !\3\2\2\2!\"\5\4\3\2\"\3\3\2\2\2#$\5\6\4\2$%\5\b\5\2")
        buf.write(u"%&\5\n\6\2&\'\5\f\7\2\'(\5\16\b\2()\5\20\t\2)\5\3\2\2")
        buf.write(u"\2*+\7\3\2\2+,\7\4\2\2,-\7\17\2\2-\7\3\2\2\2./\7\5\2")
        buf.write(u"\2/\60\7\4\2\2\60\61\7\r\2\2\61\t\3\2\2\2\62\63\7\6\2")
        buf.write(u"\2\63\64\7\4\2\2\64\65\7\17\2\2\65\13\3\2\2\2\66\67\7")
        buf.write(u"\7\2\2\678\7\4\2\289\7\17\2\29\r\3\2\2\2:<\t\2\2\2;:")
        buf.write(u"\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\17\3\2\2\2?A")
        buf.write(u"\t\2\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\21")
        buf.write(u"\3\2\2\2DE\7\n\2\2EF\7\17\2\2FG\5\24\13\2GH\7\13\2\2")
        buf.write(u"HI\7\17\2\2I\23\3\2\2\2JK\7\17\2\2KL\7\b\2\2LM\5\26\f")
        buf.write(u"\2MN\7\t\2\2NP\3\2\2\2OJ\3\2\2\2PS\3\2\2\2QO\3\2\2\2")
        buf.write(u"QR\3\2\2\2R\25\3\2\2\2SQ\3\2\2\2TU\7\17\2\2UW\7\f\2\2")
        buf.write(u"VT\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX")
        buf.write(u"\3\2\2\2[\\\7\17\2\2\\\27\3\2\2\2\b\33\37=BQX")
        return buf.getvalue()


class ClingoParser ( Parser ):

    grammarFileName = "Clingo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'Models'", u"':'", u"'Optimum'", u"'Optimization'", 
                     u"'Calls'", u"'('", u"')'", u"'Answer:'", u"'Optimization:'", 
                     u"','", u"<INVALID>", u"'OPTIMUM FOUND'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"OPTIMUM_FOUND_OR_NOT", 
                      u"OPTIMUM_FOUND", u"TEXT", u"WHITESPACE" ]

    RULE_clingoOutput = 0
    RULE_summary = 1
    RULE_models = 2
    RULE_optimum = 3
    RULE_optimization = 4
    RULE_calls = 5
    RULE_time = 6
    RULE_cpuTime = 7
    RULE_solution = 8
    RULE_actual_soln = 9
    RULE_custom_representation_soln = 10

    ruleNames =  [ u"clingoOutput", u"summary", u"models", u"optimum", u"optimization", 
                   u"calls", u"time", u"cpuTime", u"solution", u"actual_soln", 
                   u"custom_representation_soln" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    OPTIMUM_FOUND_OR_NOT=11
    OPTIMUM_FOUND=12
    TEXT=13
    WHITESPACE=14

    def __init__(self, input, output=sys.stdout):
        super(ClingoParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ClingoOutputContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.ClingoOutputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def summary(self):
            return self.getTypedRuleContext(ClingoParser.SummaryContext,0)


        def solution(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.SolutionContext)
            else:
                return self.getTypedRuleContext(ClingoParser.SolutionContext,i)


        def OPTIMUM_FOUND(self):
            return self.getToken(ClingoParser.OPTIMUM_FOUND, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_clingoOutput

        def enterRule(self, listener):
            if hasattr(listener, "enterClingoOutput"):
                listener.enterClingoOutput(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitClingoOutput"):
                listener.exitClingoOutput(self)




    def clingoOutput(self):

        localctx = ClingoParser.ClingoOutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_clingoOutput)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.T__7:
                self.state = 22
                self.solution()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ClingoParser.OPTIMUM_FOUND:
                self.state = 28
                self.match(ClingoParser.OPTIMUM_FOUND)


            self.state = 31
            self.summary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SummaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.SummaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def models(self):
            return self.getTypedRuleContext(ClingoParser.ModelsContext,0)


        def optimum(self):
            return self.getTypedRuleContext(ClingoParser.OptimumContext,0)


        def optimization(self):
            return self.getTypedRuleContext(ClingoParser.OptimizationContext,0)


        def calls(self):
            return self.getTypedRuleContext(ClingoParser.CallsContext,0)


        def time(self):
            return self.getTypedRuleContext(ClingoParser.TimeContext,0)


        def cpuTime(self):
            return self.getTypedRuleContext(ClingoParser.CpuTimeContext,0)


        def getRuleIndex(self):
            return ClingoParser.RULE_summary

        def enterRule(self, listener):
            if hasattr(listener, "enterSummary"):
                listener.enterSummary(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSummary"):
                listener.exitSummary(self)




    def summary(self):

        localctx = ClingoParser.SummaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_summary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.models()
            self.state = 34
            self.optimum()
            self.state = 35
            self.optimization()
            self.state = 36
            self.calls()
            self.state = 37
            self.time()
            self.state = 38
            self.cpuTime()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ModelsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.ModelsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_models

        def enterRule(self, listener):
            if hasattr(listener, "enterModels"):
                listener.enterModels(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitModels"):
                listener.exitModels(self)




    def models(self):

        localctx = ClingoParser.ModelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_models)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ClingoParser.T__0)
            self.state = 41
            self.match(ClingoParser.T__1)
            self.state = 42
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimumContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.OptimumContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OPTIMUM_FOUND_OR_NOT(self):
            return self.getToken(ClingoParser.OPTIMUM_FOUND_OR_NOT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_optimum

        def enterRule(self, listener):
            if hasattr(listener, "enterOptimum"):
                listener.enterOptimum(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOptimum"):
                listener.exitOptimum(self)




    def optimum(self):

        localctx = ClingoParser.OptimumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optimum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ClingoParser.T__2)
            self.state = 45
            self.match(ClingoParser.T__1)
            self.state = 46
            self.match(ClingoParser.OPTIMUM_FOUND_OR_NOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptimizationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.OptimizationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_optimization

        def enterRule(self, listener):
            if hasattr(listener, "enterOptimization"):
                listener.enterOptimization(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOptimization"):
                listener.exitOptimization(self)




    def optimization(self):

        localctx = ClingoParser.OptimizationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optimization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ClingoParser.T__3)
            self.state = 49
            self.match(ClingoParser.T__1)
            self.state = 50
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.CallsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(ClingoParser.TEXT, 0)

        def getRuleIndex(self):
            return ClingoParser.RULE_calls

        def enterRule(self, listener):
            if hasattr(listener, "enterCalls"):
                listener.enterCalls(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCalls"):
                listener.exitCalls(self)




    def calls(self):

        localctx = ClingoParser.CallsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_calls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ClingoParser.T__4)
            self.state = 53
            self.match(ClingoParser.T__1)
            self.state = 54
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.TimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_time

        def enterRule(self, listener):
            if hasattr(listener, "enterTime"):
                listener.enterTime(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTime"):
                listener.exitTime(self)




    def time(self):

        localctx = ClingoParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 56
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__1) | (1 << ClingoParser.T__5) | (1 << ClingoParser.T__6) | (1 << ClingoParser.TEXT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 59 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CpuTimeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.CpuTimeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_cpuTime

        def enterRule(self, listener):
            if hasattr(listener, "enterCpuTime"):
                listener.enterCpuTime(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCpuTime"):
                listener.exitCpuTime(self)




    def cpuTime(self):

        localctx = ClingoParser.CpuTimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cpuTime)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__1) | (1 << ClingoParser.T__5) | (1 << ClingoParser.T__6) | (1 << ClingoParser.TEXT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ClingoParser.T__1) | (1 << ClingoParser.T__5) | (1 << ClingoParser.T__6) | (1 << ClingoParser.TEXT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SolutionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.SolutionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def actual_soln(self):
            return self.getTypedRuleContext(ClingoParser.Actual_solnContext,0)


        def getRuleIndex(self):
            return ClingoParser.RULE_solution

        def enterRule(self, listener):
            if hasattr(listener, "enterSolution"):
                listener.enterSolution(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSolution"):
                listener.exitSolution(self)




    def solution(self):

        localctx = ClingoParser.SolutionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_solution)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ClingoParser.T__7)
            self.state = 67
            self.match(ClingoParser.TEXT)
            self.state = 68
            self.actual_soln()
            self.state = 69
            self.match(ClingoParser.T__8)
            self.state = 70
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Actual_solnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.Actual_solnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def custom_representation_soln(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ClingoParser.Custom_representation_solnContext)
            else:
                return self.getTypedRuleContext(ClingoParser.Custom_representation_solnContext,i)


        def getRuleIndex(self):
            return ClingoParser.RULE_actual_soln

        def enterRule(self, listener):
            if hasattr(listener, "enterActual_soln"):
                listener.enterActual_soln(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitActual_soln"):
                listener.exitActual_soln(self)




    def actual_soln(self):

        localctx = ClingoParser.Actual_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_actual_soln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ClingoParser.TEXT:
                self.state = 72
                self.match(ClingoParser.TEXT)
                self.state = 73
                self.match(ClingoParser.T__5)
                self.state = 74
                self.custom_representation_soln()
                self.state = 75
                self.match(ClingoParser.T__6)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Custom_representation_solnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ClingoParser.Custom_representation_solnContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self, i=None):
            if i is None:
                return self.getTokens(ClingoParser.TEXT)
            else:
                return self.getToken(ClingoParser.TEXT, i)

        def getRuleIndex(self):
            return ClingoParser.RULE_custom_representation_soln

        def enterRule(self, listener):
            if hasattr(listener, "enterCustom_representation_soln"):
                listener.enterCustom_representation_soln(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCustom_representation_soln"):
                listener.exitCustom_representation_soln(self)




    def custom_representation_soln(self):

        localctx = ClingoParser.Custom_representation_solnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_custom_representation_soln)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.match(ClingoParser.TEXT)
                    self.state = 83
                    self.match(ClingoParser.T__9) 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 89
            self.match(ClingoParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





