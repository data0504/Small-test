import re
import datetime

class MinConvert:
    """搞笑分鐘轉換"""
    def __init__(self) -> None:
        """建構式"""
        self.min: int = 0
        self.sec: int = 0
        self.convertUnit: int = 60
        self.firstTime:datetime.datetime = datetime.datetime.now()
        self.start: bool = True
        
    def cleanTime(self) -> None:
        """分秒初始化"""
        self.min = 0
        self.sec = 0
        
    def title(self) -> None:
        """程式標題"""
        title: str = '分轉秒換算器'; print(title)

    def userInput(self) -> int:
        """使用者輸入,str 轉換 int"""
        while self.start:
            try:
                # 使用者鍵入值
                _userInput: str = input(
                                    '輸入正整分鐘數:')
                # 正規表達,清洗數字以外的值
                _re_userValue: str = int(
                                    re.sub(r'[\D*?]','', _userInput))

                self.start = False
            except (Exception, SystemExit, GeneratorExit) as e:
                print(f'Error: 請輸入數字[0-9]\nError: {e}')
            else:
                return _re_userValue

    def parse(self, useMin:int) -> bool:
        """輸入值解析"""
        _convertSec: str = str(self.convertUnit * useMin)
        _secLen: int = int(len(_convertSec))
        _cutMinSec: int = _secLen - 2

        if _secLen <= 2 :
            self.min = self.min
            self.sec = _convertSec
        else:
            self.min = _convertSec[0:_cutMinSec]
            self.sec = _convertSec[_cutMinSec:]
        
        self.start = (_secLen > 5) == False
        return _secLen > 5

    def resolve(self, stuate: bool) -> None:
        """顯示換算成果"""
        _resolve: str = ''
        _resolve += f'{self.min}分'
        _resolve += f'{self.sec}秒。'
        print(_resolve)

        if stuate:
            _timeTotal = datetime.datetime.now() - self.firstTime
            print(f'恭喜你浪費人生 {_timeTotal.seconds}秒, 還有更有意義的事可以做XDD。')

    def execution(self) -> None:
        """執行流程"""
        self.title()
        while self.start:
            self.resolve(self.parse(self.userInput()))
            self.cleanTime()

MCS:object = MinConvert()
MCS.execution()