package com.anas.easy;

public class RomanToInteger {
    public int romanToInt(String s) {
        int num = 0;
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)) {
                case 'i' -> num++;
                case 'v' -> num += v(s, i);
                case 'x' -> num += x(s, i);
                case 'l' -> num += 50;
                case 'c' -> num += 100;
                case 'd' -> num += 500;
                case 'm' -> num += 1000;
            }
        }
        return num;
    }

    private int x(String s, int i) {
        if (i != 0 && s.charAt(i) ==)
    }

    private int v(String s, int i) {
        if (i != 0 && s.charAt(i - 1) == 'i')
            return  4;
        else
            return 5;
    }
}
