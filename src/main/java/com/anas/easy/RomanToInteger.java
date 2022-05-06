package com.anas.easy;
public class RomanToInteger {
    public int romanToInt(String s) {
        int num = 0;
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            num += getNum(s, i);
        }
        return num;
    }

    private int getNum(String s, int i) {
        int returnVal = getIntNum(s.charAt(i));
        if (i != 0) {
            short currenNum = (short) returnVal;
            short prevNum = getIntNum(s.charAt(i - 1));
            if (currenNum > prevNum) {
                returnVal = 0;
                returnVal -= prevNum;
                returnVal += (currenNum - prevNum);
            }
        }
        return returnVal;
    }

    private short getIntNum(char charAt) {
        return switch (charAt) {
            case 'v' -> 5;
            case 'x' -> 10;
            case 'l' -> 50;
            case 'c' -> 100;
            case 'd' -> 500;
            case 'm' -> 1000;
            default -> 1;
        };
    }

    public static void main(String[] args) {
        System.out.println("MCMXCIV = " + new RomanToInteger().romanToInt("MCMXCIV") );
    }
}
