package atlasEarthCalc;

import java.io.FileNotFoundException;
import java.util.Random;

public class calc {
	
	
	public static double income = 0;
	public static double incomeRate = 0;
	public static double plotCount = 0;
	public static double plotcommon = 0;
	public static double plotrare = 0;
	public static double plotepic = 0;
	public static double plotlegend = 0;
	public static double adsWatched = 0;
	public static int multiplier = 30;
	public static int bucks = 100;
	public static int TIME = 525600 * 2; // how many total minutes to run the sim for. 525,600 is one year
	
	public static void main(String[] args) {
		int minutes = 0;
		
		buyPlot();
		while (minutes < TIME) {
			minutes += 20;
			adsWatched +=1;
			bucks += 2;
			if(minutes % 60 == 0) {
				adsWatched++;
			}
			if(minutes % 1440 == 0) {
				bucks++;
			}
			getRent();
			if (bucks >= 100) {
				buyPlot();
			}
		}
		
		
		printSummary();
	}
	
	public static void printSummary() {
		System.out.println("you spent "+ (adsWatched * .45)/60 +" hours watching " + adsWatched +" ads");
		System.out.println("you bought " + plotcommon + " common plots, " + plotrare + " rare plots, " 
				+ plotepic + " epic plots,and "+ plotlegend + " legendary plots, for a total of " + plotCount +" plots");
		System.out.println("you earned $" + income + " with an average ad watched per dollar earned of " + adsWatched/income);
	}
	
	public static void getRent() {
		income += incomeRate * 1200 *multiplier;
	}
	
	
	public static void buyPlot() {
		bucks -= 100;
		Random r = new Random();
		int p = r.nextInt(100);
		if (p <50) {
			incomeRate += .0000000011; 
			plotcommon++;
		}
		if (80 >= p && p >= 50) {
			incomeRate += .0000000016; 
			plotrare++;
		}
		if (95 >= p && p > 80) {
			incomeRate += .0000000022; 
			plotepic++;
		}
		if (p > 95) {
			incomeRate += .0000000044;
			plotlegend++;
		}
		plotCount += 1;
		
		if (plotCount > 150) {
			multiplier = 20;
		}
		if (plotCount > 220) {
			multiplier = 15;
		}
		if (plotCount > 290) {
			multiplier = 12;
		}
		if (plotCount > 365) {
			multiplier = 10;
		}
		if (plotCount > 435) {
			multiplier = 8;
		}
		if (plotCount > 545) {
			multiplier = 7;
		}
	}

}
