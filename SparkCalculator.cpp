#include<iostream>
#include<string>
using namespace std;

double TotalDraws(double crystals, double tix, double tenrolls){
    double TotalDraws = (tix * 300 + tenrolls * 3000 + crystals) / 300;
    return TotalDraws;
}

string HowManyRolls(double Total){
    if(Total > 300){
        int LeftoverInt = Total - 300;
        string Leftover = to_string(LeftoverInt);
        string message = "You can spark a character and have " + Leftover + " draws leftover to draw for whomever you want!";
        return message;
    } else if(Total < 300){
        int UntilCanSparkInt = 300 - Total;
        string UntilCanSpark = to_string(UntilCanSparkInt);
        string message = "Sorry, you need " + UntilCanSpark + " draws until you can spark a character...";
        return message;
    } else{
        string message = "You can spark a character!";
        return message;
    }
}

string SparkCalculator(double crystals, double tix, double tenrolls){
    int smack = TotalDraws(crystals, tix, tenrolls);
    string total = to_string(smack);
    string message = "You can make a total of " + total + " draws.";
    return message;
}

bool TestForNegative(int num){
    if(num < 0){
        return true;
    } else{
        return false;
    }
}

int main(){
    double crystals;
    double tix;
    double tenrolls;
    cout << "Welcome to Spark Calculator" << endl;
    cout << "How many crystals do you have?" << endl;
    cin >> crystals;
    cout << "How many single roll tickets do you have?" << endl;
    cin >> tix;
    cout << "Finally, how many 10 roll tickets do you have?" << endl;
    cin >> tenrolls;
    double Total = TotalDraws(crystals, tix, tenrolls);
    cout << SparkCalculator(crystals, tix, tenrolls) << endl;
    cout << HowManyRolls(Total) << endl;
}

