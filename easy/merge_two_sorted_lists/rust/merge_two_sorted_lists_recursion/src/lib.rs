#[derive(PartialEq, Eq, Debug, Clone)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }

    // For testing only
    pub fn add_node(&mut self, node: ListNode) -> Self {
        match self.next {
            Some(ref mut n) => { n.add_node(node); }
            None => self.next = Some(Box::new(node)),
        };
        self.clone()
    }
}

impl Iterator for ListNode {
    type Item = Box<ListNode>;

    fn next(&mut self) -> Option<Self::Item> {
        self.next.to_owned()
    }
}

struct Solution {}

impl Solution {
    pub fn merge_two_lists(list1: Option<Box<ListNode>>, list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let Some(mut list1_head) = list1 else {
            return list2
        };

        let Some(mut list2_head) = list2 else {
            return Some(list1_head)
        };

        if list1_head.val < list2_head.val {
            list1_head.next = Solution::merge_two_lists(list1_head.next, Some(list2_head));
            return Some(list1_head);
        } else {
            list2_head.next = Solution::merge_two_lists(Some(list1_head), list2_head.next);
            return Some(list2_head)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn case_1() {
        let head_of_list_1 = ListNode::new(1)
            .add_node(ListNode::new(2))
            .add_node(ListNode::new(4));

        println!("The first list is: {head_of_list_1:#?}");

        let head_of_list_2 = ListNode::new(1)
            .add_node(ListNode::new(3))
            .add_node(ListNode::new(4));

        println!("The second list is {head_of_list_2:#?}");

        let merged_list = Solution::merge_two_lists(Some(Box::new(head_of_list_1)),
                                                    Some(Box::new(head_of_list_2)));

        let correct_list = ListNode::new(1)
            .add_node(ListNode::new(1))
            .add_node(ListNode::new(2))
            .add_node(ListNode::new(3))
            .add_node(ListNode::new(4))
            .add_node(ListNode::new(4));

        assert_eq!(merged_list, Some(Box::new(correct_list)));
    }

    #[test]
    fn case_2() {
        assert_eq!(Solution::merge_two_lists(None, None), None);
    }

    #[test]
    fn case_3() {
        assert_eq!(Solution::merge_two_lists(None, Some(Box::new(ListNode::new(0)))),
                   Some(Box::new(ListNode::new(0))));
    }


    #[test]
    fn case_4() {
        let head_of_list_1 = ListNode::new(1)
            .add_node(ListNode::new(2))
            .add_node(ListNode::new(3));

        println!("The first list is: {head_of_list_1:#?}");

        let head_of_list_2 = ListNode::new(4)
            .add_node(ListNode::new(5))
            .add_node(ListNode::new(6));

        println!("The second list is {head_of_list_2:#?}");

        let merged_list = Solution::merge_two_lists(Some(Box::new(head_of_list_1)),
                                                    Some(Box::new(head_of_list_2)));

        let correct_list = ListNode::new(1)
            .add_node(ListNode::new(2))
            .add_node(ListNode::new(3))
            .add_node(ListNode::new(4))
            .add_node(ListNode::new(5))
            .add_node(ListNode::new(6));

        assert_eq!(merged_list, Some(Box::new(correct_list)));
    }
}
