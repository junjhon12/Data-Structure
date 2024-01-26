public class week3{
    public static void main(String[] args) {
        
        // What we understand of Big O is that it is a way to measure the efficiency of an algorithm
        // Worse case scenario is log_2(n) where n is the number of elements in the array
        // nlog_2(n) is the average case scenario, n for
        
        String[] A = {"eat", "tea", "tan", "ate", "nat", "bat"};
        // Output should be [["ate","eat","tea"],["nat","tan"],["bat"]]
    }

    public static void groupAnagrams(String[] A) {
        //dictionary = {}
        //for S in A:
        // count = [0] * 26
        // for l in s:
        //  count[ord(l) - ord('a')] += 1
        // if tuple(count) not in dictionary:
        // dictionary[tuple(count)] = []
        // dictionary[tuple(count)].append(s)
        // return dictionary.values()

        // n -> number of elements in input
        // m -> average length

        Disctionary<String, List<String>> dictionary = new HashMap<>();
        for(String s : A){
            int[] count = new int[26];
            for(char l : s.toCharArray()){
                count[l - 'a']++;
            }
            String key = Arrays.toString(count);
            if(!dictionary.containsKey(key)){
                dictionary.put(key, new ArrayList<>());
            }
            dictionary.get(key).add(s);
        }
        return new ArrayList<>(dictionary.values());
    }
}