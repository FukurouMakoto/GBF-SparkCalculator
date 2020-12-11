//This is an attempt to create a C# conversion of the GBF Spark Calculator Program
using System;
namespace GBF_SparkCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Spark Calculator");
            Console.WriteLine("How many crystals do you have?");
            double crystals = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("How many single roll tickets do you have?");
            double tix = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Finally, how many 10 roll tickets do you have?");
            double tenrolls = Convert.ToDouble(Console.ReadLine());
            double Total = TotalDraws(crystals, tix, tenrolls);
            Console.WriteLine(SparkCalculator(crystals, tix, tenrolls));
            Console.WriteLine(HowManyRolls(Total));

        }

        static double TotalDraws(double crystals, double tix, double tenrolls)
        {
            double TotalDraws = ((tix * 300) + (tenrolls * 3000) + crystals) / 300;
            return TotalDraws; /*Working Correctly */
        }
        static string HowManyRolls(double Total)/*This code is working */
        {
            if(Total > 300)
            {
                int Leftover = Convert.ToInt32(Total) - 300;
                string message = "You can spark a character and have " + Convert.ToString(Leftover) + " draws leftover to draw for whomever you want!";
                return message;
            } else if(Total < 300)
            {
                int UntilCanSpark = 300 - Convert.ToInt32(Total);
                string message = "Sorry, you need " + Convert.ToString(UntilCanSpark)+ " draws until you can spark a character...";
                return message;
            } else
            {
                string message = "You can spark a character!";
                return message;
            }
        }

        static string SparkCalculator(double crystals, double tix, double tenrolls)
        {
            string message = "You can make a total of " + Convert.ToString(Convert.ToInt32(TotalDraws(crystals, tix, tenrolls))) + " draws.";
            return message;
        }

        static bool TestForNegative(int num)
        {
            if(num < 0){
                return true;
            } else
            {
                return false;
            }
        }
    }
}
