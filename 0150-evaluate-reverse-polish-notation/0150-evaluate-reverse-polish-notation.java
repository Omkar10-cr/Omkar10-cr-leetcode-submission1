class Solution {
    public int evalRPN(String[] tokens) {
        int[] stack = new int[tokens.length];
        int top = 0;
        for (String t : tokens) {
            if (t.equals("+") || t.equals("-") || t.equals("*") || t.equals("/")) {
                int b = stack[--top];
                int a = stack[--top];
                if (t.equals("+")) stack[top++] = a + b;
                else if (t.equals("-")) stack[top++] = a - b;
                else if (t.equals("*")) stack[top++] = a * b;
                else stack[top++] = a / b;
            } else {
                stack[top++] = Integer.parseInt(t);
            }
        }
        return stack[0];
    }
}