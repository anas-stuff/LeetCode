package com.anas.leetcode.easy;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String commonPrefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            String str = strs[i];
            if (commonPrefix.length() > str.length()) // if common prefix length less than str length
                commonPrefix = commonPrefix.substring(0, str.length()); // set common prefix to str length
            for (int j = commonPrefix.length() - 1; j >= 0; j--) {
                if (commonPrefix.charAt(j) != str.charAt(j)) {
                    commonPrefix = commonPrefix.substring(0, j); // remove char
                    j = commonPrefix.length(); // update j
                }

            }
        }
        return commonPrefix;
    }

    public static void main(String[] args) {
        LongestCommonPrefix lo = new LongestCommonPrefix();
        // Test 2
        System.out.println(lo.longestCommonPrefix(new String[]{"flower","flow","flight"}));
        // Test 1
        System.out.println(lo.longestCommonPrefix(new String[]{"dog","racecar","car"}));
        // Test 3
        System.out.println(lo.longestCommonPrefix(new String[]{"cir","car"}));
    }
}
