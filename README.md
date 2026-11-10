CS526 Homework 5

Problem 1
Use python Problem 1.py for a fresh randomized run.

Problem 2 (paste as one line)
python Problem 2.py inputs/vowel_input1.txt inputs/vowel_input2.txt inputs/vowel_input3.txt inputs/vowel_input4.txt

Problem 3 (paste as one line)
python Problem 3.py inputs/longest_seq1.txt inputs/longest_seq2.txt inputs/longest_seq3.txt inputs/longest_seq4.txt inputs/longest_seq5.txt inputs/longest_seq6.txt

For Problems 2 and 3, you can also pass a single input file. The
screenshots show one run for each problem.


PROBLEM 1
Node stores a value and references to its left and right children.
BST stores the root. AddNode and FindNode follow the left branch for
smaller values and the right branch for larger ones. The tree stores
one node per value. FindNode returns the node if found, or None.

DeleteNode follows the search path to the target. It removes a leaf
or promotes the only child. If the node has two children, it uses
the largest value in the left subtree (the inorder predecessor),
following Lecture 6 Part 1, then deletes the predecessor's old node.
PrintTree uses indentation and L/R labels to show the branches.

The demo samples 5 to 50 distinct integers from 1 through 1000. It
prints the initial tree, adds a randomly chosen unused value, and
deletes the original root. It prints the tree after each change
and chooses one present value and one absent value for the searches.

Add, delete, and find each take O(h) time for tree height h. PrintTree
visits all n nodes and indents each line by its node's depth.


PROBLEM 2
I used bottom-up dynamic programming from Lecture 6 Part 2. ways[i]
counts the ways to decode the first i symbols using only vowels.
ways[0] = 1 because the empty prefix has one decoding. For each i,
I try all five vowel codes as the last letter. If a code of length k
matches the end of the prefix, I add ways[i-k] to ways[i]. Each
decoding has exactly one last letter, so this counts every valid
decoding once. The answer is ways[n], where n is the input length.
The algorithm uses O(n) steps and O(n) table entries.


PROBLEM 3
I used two bottom-up DP arrays. length_a[i] is the longest valid
sequence that ends at A[i]. length_b[i] is defined the same way for
B[i]. Both start at 1 because each element can start a sequence.
I process positions in increasing order. For A[i], I check each
B[j] where j < i and B[j] < A[i]. That lets me append A[i] to the
sequence ending at B[j]. I do the same with A and B swapped for B[i].

Looking only at the other array enforces alternation. Checking j < i
enforces the position rule even when switching arrays, and comparing
values strictly enforces the increase. Each valid sequence ending at
a given element either starts there or extends one of the endings
checked by the loops. I save each best previous index so I can
reconstruct an actual sequence. The command prints its length,
as shown in the assignment examples.

For sizes m and n, the DP takes O(m*n + m + n) time and O(m + n)
space. Expected lengths for files 1 through 6 are 4, 7, 10, 39,
192, and 1.
