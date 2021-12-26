package Java;
class ReverseWordsInString {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            if (words[i].length() > 0) {
                sb.append(words[i]);
                sb.append(" ");
            }
        }
        return sb.toString().trim();
    }
    public static void main(String[] args) {
        ReverseWordsInString r = new ReverseWordsInString();
        System.out.println(r.reverseWords("Hii Harsh... How are you? You can insert as many spaces you want in this string. Trim function will remove the extra spaces."));
    }
}