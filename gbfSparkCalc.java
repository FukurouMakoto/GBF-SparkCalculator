import java.util.Scanner;


public class gbfSparkCalc {
	
	public static int getCrystals() //get crystal amount from user
	{
		Scanner x = new Scanner(System.in);
		System.out.println("How many crystals do you have? ");
		String crys = x.nextLine();
		int crystals = Integer.valueOf(crys);
		return crystals;
	}
	public static int getSingleTickets() //get single ticket amount from user
	{
		Scanner y = new Scanner(System.in);
		System.out.println("How many single tickets do you have? ");
		String tix = y.nextLine();
		int singleTickets = Integer.valueOf(tix);
		return singleTickets;
	}
	public static int getTenTickets() //get ten ticket amount from user
	{
		Scanner z = new Scanner(System.in);
		System.out.println("How many ten tickets do you have? ");
		String ten = z.nextLine();
		int tenTix = Integer.valueOf(ten);
		return tenTix;
	}
	public static int ticketsToCrystals(int singleTickets) //convert single tix to crystals
	{
		return singleTickets * 300;
	}
	public static int tenTixToCrystals(int tenTix)
	{
		return tenTix * 3000;
	}

	public static int crystalsTotal(int crystals, int singleTickets, int tenTix) //Add everything up
	{
		int total = crystals + singleTickets + tenTix;
		return total;
	}
	public static boolean sparkTest(int total) //Can the user spark?
	{
		if(total >= 90000)
		{
			return true;
		}else
		{
			return false;
		}
	}
	public static String message(boolean status)
	{
		if(status == true)
		{
			return "Yes, you have enough to spark!";
		}
		else
		{
			return "Sorry, you do not have enough to spark...";
		}
	}
	public static String overspark(int total)
	{
		total -= 90000;
		total /= 300;
		String totals = String.valueOf(total);
		return "You have enough extra crystal to roll " + totals + " more times!";
	}
	public static String notEnough(int total)
	{
		int spark = 90000;
		spark -= total;
		spark /= 300;
		String result = String.valueOf(spark);
		return "You are " + result + " rolls short to be able to spark.";
	}
	public static void main(String[] args)
	{
		int crystals, singleTickets, tenTix;
		crystals = getCrystals();
		singleTickets = getSingleTickets();
		tenTix = getTenTickets();
		singleTickets = ticketsToCrystals(singleTickets);
		tenTix = tenTixToCrystals(tenTix);
		int total = crystalsTotal(crystals, singleTickets, tenTix);
		if(sparkTest(total))
		{
			System.out.println(message(sparkTest(total)));
			System.out.println(overspark(total));
		}else
		{
			System.out.println(message(sparkTest(total)));
			System.out.println(notEnough(total));
		}

	}

}

