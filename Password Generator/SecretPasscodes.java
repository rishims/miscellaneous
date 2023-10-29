/** This program generates a random passcode for the user based on his/her preferences.
 * 
 * @author Rishi Shah
 * @version 10/09/19
 */
import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;
public class SecretPasscodes
{ 
    public static void main(String[] args) throws IOException
    {
      Scanner in = new Scanner(System.in);
      PrintWriter passcodeFile = new PrintWriter(new File("passcodes.txt"));
      
      int userSelection = 0;
      int userPasscodeLength = 0;
      
      System.out.println("\t\t      Password Generator Menu");
      System.out.println("********************************************************************");
      System.out.println("*     [1] Lowercase Letters                                        *");
      System.out.println("*     [2] Lowercase and Capital Letters                            *");
      System.out.println("*     [3] Lowercase and Capital Letters and Numbers                *");
      System.out.println("*     [4] Lowercase and Capital Letters, Numbers, and Symbols      *");
      System.out.println("*     [5] Quit                                                     *");
      System.out.println("********************************************************************");
      
      System.out.print("\nEnter Selection (1-5): ");
      userSelection = in.nextInt();
      while (!(userSelection >= 1 && userSelection <= 5))
      {
        System.out.println("  Invalid selection. Please try again.");
        System.out.print("\nEnter Selection (1-5): ");
        userSelection = in.nextInt();
      }
      
      if (userSelection == 5)
      {
            
            passcodeFile.close();
      }
      
      else 
      {
            System.out.print("Password Length (6 or more): ");
            userPasscodeLength = in.nextInt();
            while (userPasscodeLength < 6)
            {
                System.out.println("  Password length too short. Please try again.");
                System.out.print("Password Length (6 or more): ");
                userPasscodeLength = in.nextInt();
            }
      }
      
      if (userSelection == 1)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(passcodeCharacter >= 97 && passcodeCharacter <= 122))   //lowercase letters ASCII VALUES
            {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(passcodeCharacter >= 97 && passcodeCharacter <= 122))   //lowercase letters ASCII VALUES
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
                 
                
      }
      
        if (userSelection == 2)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90)
            ))   //lowercase and uppercase letters ASCII values
            {                                                                                                                           
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
                    (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
                    || (passcodeCharacter >= 65 && passcodeCharacter <= 90)
                    ))   
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
            
                
      }
      
      if (userSelection == 3)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            ))                                                                           //lowercase and uppercase letters and numbers
            {                                                                                                                          
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            )) 
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
                 
                
      }
      
        if (userSelection == 4)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            || (passcodeCharacter >= 58 && passcodeCharacter <= 64)
            ))                                                                           //lowercase and uppercase letters and numbers and symbols
            {                                                                                                                          
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            || (passcodeCharacter >= 58 && passcodeCharacter <= 64)
            )) 
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
               
                
      }
     
    if(userSelection != 5)
    { System.out.print("\nEnter Selection (1-5): ");
      userSelection = in.nextInt();
      while (!(userSelection >= 1 && userSelection <= 5))
      {
        System.out.println("  Invalid selection. Please try again.");
        System.out.print("\nEnter Selection (1-5): ");
        userSelection = in.nextInt();
      }  
    }
    
      if (userSelection == 5)
      {
            System.out.println("\nThank you for using the Passcode Generator.");
            passcodeFile.close();
      }
      
      else 
      {
            System.out.print("Password Length (6 or more): ");
            userPasscodeLength = in.nextInt();
            while (userPasscodeLength < 6)
            {
                System.out.println("  Password length too short. Please try again.");
                System.out.print("Password Length (6 or more): ");
                userPasscodeLength = in.nextInt();
            }
      }
      
      
      passcodeFile.println();
      
      
   while (userSelection != 5 && userSelection >= 1 && userSelection <= 5)
    {  
      if (userSelection == 1)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(passcodeCharacter >= 97 && passcodeCharacter <= 122))   //lowercase letters ASCII VALUES
            {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(passcodeCharacter >= 97 && passcodeCharacter <= 122))   //lowercase letters ASCII VALUES
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
              
                
      }
      
        if (userSelection == 2)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90)
            ))   //lowercase and uppercase letters ASCII values
            {                                                                                                                           
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
                    (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
                    || (passcodeCharacter >= 65 && passcodeCharacter <= 90)
                    ))   
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
                
                
      }
      
      if (userSelection == 3)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            ))                                                                           //lowercase and uppercase letters and numbers
            {                                                                                                                          
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            )) 
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
                
                
      }
      
        if (userSelection == 4)
      {
            int passcodeLength = 0;
            Random randNum = new Random();
            int passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
            while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            || (passcodeCharacter >= 58 && passcodeCharacter <= 64)
            ))                                                                           //lowercase and uppercase letters and numbers and symbols
            {                                                                                                                          
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
            }
          
            passcodeFile.print((char)passcodeCharacter);
            passcodeLength++;
            while (passcodeLength < userPasscodeLength)
            {
                passcodeCharacter = randNum.nextInt(128);       //ASCII values range from 0-128
          
                    while ( !(
            (passcodeCharacter >= 97 && passcodeCharacter <= 122) 
            || (passcodeCharacter >= 65 && passcodeCharacter <= 90) 
            || (passcodeCharacter >= 48 && passcodeCharacter <= 57)
            || (passcodeCharacter >= 58 && passcodeCharacter <= 64)
            )) 
                {
                 
                 passcodeCharacter = randNum.nextInt(128);        
            
                }
          
                passcodeFile.print((char)passcodeCharacter);
                passcodeLength++;
            }                           
                
                
      }
      
      System.out.print("\nEnter Selection (1-5): ");
      userSelection = in.nextInt();
      while (!(userSelection >= 1 && userSelection <= 5))
      {
        System.out.println("  Invalid selection. Please try again.");
        System.out.print("\nEnter Selection (1-5): ");
        userSelection = in.nextInt();
      }  
      
      if (userSelection == 5)
      {
            System.out.println("\nThank you for using the Passcode Generator.");
            passcodeFile.close();
      }
      
      else 
      {
            System.out.print("Password Length (6 or more): ");
            userPasscodeLength = in.nextInt();
            while (userPasscodeLength < 6)
            {
                System.out.println("  Password length too short. Please try again.");
                System.out.print("Password Length (6 or more): ");
                userPasscodeLength = in.nextInt();
            }
      }
      
      
      passcodeFile.println();
      
      
    }  
    
    File filePasscodeFile = new File("passcodes.txt");
    Scanner inPasscodeFile = new Scanner(filePasscodeFile);
    
    System.out.println("\nHere are your randomly generated codes:\n ");
    int n = 0;
    
    if ( !(inPasscodeFile.hasNextLine()))
    {
        System.out.print("N/A");
    }
    
    while(inPasscodeFile.hasNextLine())
    {
        n++;
        System.out.println("  " + n + "        " + inPasscodeFile.nextLine());
    
    }
    
   }//end of main method
}//end of class 

     
   
     
