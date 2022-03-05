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
        int[] arr = {9,5,2,1,4,3};
	int max = 0;
	for(int i=0; i < arr.length; i++)
			if(max < arr[i])
				max = arr[i];
	int maxOR = 0;
	for(int i=0; i < arr.length; i++)
		if(maxOR < (max^arr[i]))
			maxOR = max^arr[i];

				
	System.out.println("Maximum XOR: " + maxOR);
    }
}
