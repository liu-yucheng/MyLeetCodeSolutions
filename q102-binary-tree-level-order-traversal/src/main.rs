use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    let tree = TreeNode {
        val: 3,
        left: Option::from(Rc::from(RefCell::from(TreeNode {
            val: 9,
            left: None,
            right: None,
        }))),
        right: Option::from(Rc::from(RefCell::from(TreeNode {
            val: 20,
            left: Option::from(Rc::from(RefCell::from(TreeNode {
                val: 15,
                left: None,
                right: None,
            }))),
            right: Option::from(Rc::from(RefCell::from(TreeNode {
                val: 7,
                left: None,
                right: None,
            }))),
        }))),
    };
    let root = Option::from(Rc::from(RefCell::from(tree)));
    let result = Solution::level_order(root);
    println!("result:{:?}", result);
}

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub struct Solution;

impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = vec![];

        match root {
            Some(rc_tree) => {
                let tree = Rc::try_unwrap(rc_tree).unwrap().into_inner();
                let mut frontier = vec![tree];
                while frontier.len() > 0 {
                    let mut level = vec![];
                    let mut new_frontier = vec![];
                    for elem in frontier {
                        level.push(elem.val);
                        match elem.left {
                            Some(rc_node) => {
                                let node = Rc::try_unwrap(rc_node).unwrap().into_inner();
                                new_frontier.push(node);
                            }
                            None => {}
                        }
                        match elem.right {
                            Some(rc_node) => {
                                let node = Rc::try_unwrap(rc_node).unwrap().into_inner();
                                new_frontier.push(node);
                            }
                            None => {}
                        }
                    }
                    result.push(level);
                    frontier = new_frontier;
                }
                return result;
            }
            None => {
                return result;
            }
        }
    }
}
