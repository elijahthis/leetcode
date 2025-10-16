class Solution:
    def intToRoman(self, num: int) -> str:
        # placeVal -> {low, mid, high}
        # Time Complexity: O(1)
        # Space Complexity: O(1)

        placeValHash = {
            1: {
                "low": "I",
                "mid": "V",
                "high": "X",
            },
            2: {
                "low": "X",
                "mid": "L",
                "high": "C",
            },
            3: {
                "low": "C",
                "mid": "D",
                "high": "M",
            },
        }

        result = ""
        valArr = list(str(num))

        def mainLogic(val, placeVal):
            result = ""
            if placeVal == 4:
                result += int(val) * "M"
            else:
                if int(val) < 4:
                    result += int(val) * placeValHash[placeVal]["low"]
                elif int(val) == 4:
                    result += placeValHash[placeVal]["low"]
                    result += placeValHash[placeVal]["mid"]
                elif int(val) == 5:
                    result += placeValHash[placeVal]["mid"]
                elif int(val) < 9:
                    result += placeValHash[placeVal]["mid"]
                    result += (int(val)-5) * placeValHash[placeVal]["low"]
                else:
                    result += placeValHash[placeVal]["low"]
                    result += placeValHash[placeVal]["high"]
            
            return result

        for i in range(len(valArr)):
            placeVal = len(valArr) - i

            result += mainLogic(valArr[i], placeVal)

        return result

