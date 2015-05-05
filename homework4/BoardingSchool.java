public class BoardingSchool {

	private static boolean[][] free = new boolean [15][15];
	private static int [][] girls = new int [5][21];
	private static final int days = 7;

	public static void main (String[] args) {
		initializeFirstDay();
		initializeThreeRows();
		printTable();
	}

	public static void printRow(int[] row) {
		for (int i = 0; i < row.length; i++) {
			girls[0][i] = row[i];
			System.out.print(girls[0][i] + "  ");
			if (i % 3 == 2 ) {
            	System.out.print("\t");
            }
		}
		System.out.println();
	}

	public static void printTable() {
		for (int row = 0; row < girls.length; row++) {
			printRow(girls[row]);
		}
	}

	public static void initializeFirstDay() {
		int counter = 0;
		for (int row = 0; row < girls.length; row++) {
			for (int column = 0; column < 3; column++) {
				girls [row][column] = counter;
				counter++;
			}
		}
	}

	public static void initializeThreeRows() {
		int counter = 0;
		for (int column = 3; column < girls[0].length; column+= 3) {
			for (int row = 0; row < 3; row++) {
				girls [row][column] = counter;
				counter++;
				if (counter > 2) {
					counter = 0;
				}
			}
		}
	}

	public static void available(int firstGirl, int secondGirl) {
		for (int row = 0; row < girls.length; row++) {
			for (int column = 0; column < girls[row].length; column++) {

			}
		}
	}

	public static boolean checkAvailability (int firstGirl, int secondGirl) {
		boolean result = false;
		for (int i = 0; i < free.length; i++) {
			for (int j = 0; j < free[i].length; i++) {
				result = free[i][j];
			}
		} 
		return result;
	}

}