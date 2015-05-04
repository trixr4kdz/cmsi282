public class SubsetSum {

    private static String errorMessage() {
        return "Please enter positive integers, with the last paramter being the potential subset sum. ";
    }
 
    public static void main(String[] args) {

        if(args.length < 1) {
            System.out.println(errorMessage());
            return;
        }
        for (int i = 0; i < args.length; i ++) {
            int valueCheck = 0;

            if(Integer.parseInt(args[i]) < 0) {
                System.out.println(errorMessage());
                return;
            }

            try {
                valueCheck = Integer.parseInt(args[i]);

            } catch(NumberFormatException nfe) {
                System.out.println("Sorray brah, integers only.");
                System.out.println(errorMessage());
                return;
            }
        }

        //special case for an empty set, being asked if it sums to 0;
        if (args.length == 1 && 0 == Integer.parseInt(args[0])) {
            System.out.println("true");
            return;
        } else if(args.length == 1 && Integer.parseInt(args[0]) != 0) {
            System.out.println("false");
            return;
        }

        int[] arrayOfNumbers = new int[args.length - 1];
        int sumValue = Integer.parseInt(args[args.length - 1]);

        for(int i = 0; i < arrayOfNumbers.length; i++) {
            arrayOfNumbers[i] = Integer.parseInt(args[i]);
        }

        boolean result = doISum(arrayOfNumbers, sumValue) ? true : false;

        System.out.println(result);

    }
    
    public static boolean doISum(int [] numberArray, int sum) {
        int len = numberArray.length;
        boolean[][] table = new boolean[sum+1][len+1];
        
        for (int i = 0; i <= len; i++ ) {
            table[0][i] = true;
        }
        
        for (int i = 1; i <= sum; i++ ){
            table[i][0] = false;
        }
        
        for (int i = 1; i <= sum; i++ ) {
            for( int j = 1; j <= len; j++ ) {
                table[i][j] = table[i][j-1]; 
                
                if (!table[i][j] && i >= numberArray[j-1]) {
                    table[i][j] = table[i-numberArray[j-1]][j-1];
                }
            }
        }

        return table[sum][len];
    }
}