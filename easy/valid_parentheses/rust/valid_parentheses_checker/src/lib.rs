struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut open_parentheses = vec![];

        // itrate over string
        for c in s.chars() {
            match c {
                '(' | '[' | '{' => open_parentheses.push(c),
                ')' | ']' | '}' => match open_parentheses.pop() {
                    Some(p) => {
                        if !Self::is_close_by(p, c) {
                            return false;
                        }
                    }
                    None => return false,
                },
                _ => (),
            }
        }

        open_parentheses.is_empty()
    }

    fn is_close_by(p: char, other: char) -> bool {
        match p {
            '(' if other == ')' => true,
            '[' if other == ']' => true,
            '{' if other == '}' => true,
            _ => false,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_1() {
        assert_eq!(Solution::is_valid("()".to_string()), true);
    }

    #[test]
    fn case_2() {
        assert_eq!(Solution::is_valid("()[]{}".to_string()), true);
    }

    #[test]
    fn case_3() {
        assert_eq!(Solution::is_valid("(]".to_string()), false);
    }

    #[test]
    fn case_4() {
        assert_eq!(
            Solution::is_valid("((([[[{{{(({({[]})}))}}}]]])))".to_string()),
            true
        );
    }

    #[test]
    fn case_5() {
        assert_eq!(
            Solution::is_valid("((([[[{{{(({({[]})}))}}}]])))".to_string()),
            false
        );
    }
}
