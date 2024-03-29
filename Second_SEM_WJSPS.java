

package com.mycompany.wjsps;

import java.util.ArrayList;
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class WJSPS {

public static void main(String[] args) {

    Scanner input = new Scanner(System.in);

    System.out.println("Welcome to WJ's Pearl Shake Cashier Registration!");
    System.out.print("Please enter your name for registration: ");
    String username = input.nextLine();
    System.out.print("Please enter a password that you can remember: ");
    String password = input.nextLine();

    System.out.println("Account created successfully!");

    System.out.println("It's time to log in!");
    while (true) {
        System.out.print("Enter your name: ");
        String inputUsername = input.nextLine();
        System.out.print("Enter your password: ");
        String inputPassword = input.nextLine();

        if (inputUsername.equals(username) && inputPassword.equals(password)) {
            System.out.println("Login successful!");
            openCashierSystem(username);
            break;
        } else {
            System.out.println("Wrong username or password. Please try again.");
        }
    }
}

public static void openCashierSystem(String username) {
    Scanner input = new Scanner(System.in);

    System.out.println("Welcome to WJ's Pearl Shake Cashier System, " + username + "!");

    Scanner scanner = new Scanner(System.in);
    String[] main_menu = {"Pearl Shakes", "Snacks", "Lemonade", "Stop Ordering"};
    String[] menu_1 = {"Chocolate Hot Fudge", "Choco Kisses", "Cookies N'Cream", "Coffee Crumble", "Mocha", "Strawberry", "Vanilla", "Avocado", "Taro", "Buko Pandan", "Ube"};
    double[] price_1 = {50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00, 50.00};
    String[] menu_2 = {"Tempura", "Fishball", "Siomai Rice", "Tornado Potato"};
    double[] price_2 = {5.00, 10.00, 25.00, 30.00};
    String[] menu_3 = {"Blue Lemonade", "Red Ice Tea Lemonade", "Cucumber Lemonade"};
    double[] price_3 = {45.00, 45.00, 45.00};

    ArrayList<String> order = new ArrayList<String>();
    ArrayList<Integer> quantity = new ArrayList<Integer>();
    ArrayList<Double> order_price = new ArrayList<Double>();

    System.out.println("Please ask the customer what menu will they be ordering from.");

    while (true) {
        System.out.println("Select a number from 1 to 3. If the customer is done ordering select number 4.");
        System.out.println("Our Menu");
        for (int i = 0; i < main_menu.length; i++) {
            System.out.println((i + 1) + "." + main_menu[i]);
        }
        System.out.print("Select Menu: ");
        String selection_num = scanner.nextLine();

        if (selection_num.equals("1")) {


            while (true) {
                    for (int i = 0; i < menu_1.length; i++) {
                        System.out.println((i + 1) + "." + menu_1[i] + " - " + price_1[i]);
                    }
                    System.out.print("Ask the customer what they would like to order (1-11): ");
                    int order_num = Integer.parseInt(scanner.nextLine());
                    if (order_num > 0 && order_num <= menu_1.length) {
                    order.add(menu_1[order_num - 1]);
                    order_price.add(price_1[order_num - 1]);
                    System.out.println("Added " + menu_1[order_num - 1] + " to their order.");
                    System.out.println("Their order: " + order);
                    System.out.println("Their order price: " + order_price);
                    System.out.print("Ask how much do they want to buy.: ");
                    int quantity_item = Integer.parseInt(scanner.nextLine());
                    quantity.add(quantity_item);
                    break;
                } else {
                    System.out.println("Invalid input. Please try again.");
                }
            }
            while (true) {
                System.out.print("Ask if they would like to order more from this menu? (type y for yes / type n for no): ");
                String choice = scanner.nextLine();
                if (choice.equalsIgnoreCase("n")) {
                    break;
                } else if (choice.equalsIgnoreCase("y")) {
                    while (true) {
                        for (int i = 0; i < menu_1.length; i++) {
                        System.out.println((i + 1) + "." + menu_1[i] + " - " + price_1[i]);
                        }
                        System.out.print("Ask the customer what they would like to order (1-11): ");
                        int order_num = Integer.parseInt(scanner.nextLine());
                        if (order_num > 0 && order_num <= menu_1.length) {
                            order.add(menu_1[order_num - 1]);
                            order_price.add(price_1[order_num - 1]);
                            System.out.println("Added " + menu_1[order_num - 1] + " to their order.");
                            System.out.println("Their order: " + order);
                            System.out.println("Their order price: " + order_price);
                            System.out.print("Ask how much do they want to buy.: ");
                            int quantity_item = Integer.parseInt(scanner.nextLine());
                            quantity.add(quantity_item);
                            break;
                        } else {
                            System.out.println("Invalid input. Please try again.");
                        }
                    } 
                    continue;
                } else {
                    System.out.println("Invalid input. Please try again.");
                    continue;
                }
            }

        } else if (selection_num.equals("2")) {
            

            while (true) {
                for (int i = 0; i < menu_2.length; i++) {
                System.out.println((i + 1) + "." + menu_2[i] + " - " + price_2[i]);
            }
                System.out.print("Ask the customer what they would like to order (1-4): ");
                int order_num = Integer.parseInt(scanner.nextLine());
                if (order_num > 0 && order_num <= menu_2.length) {
                    order.add(menu_2[order_num - 1]);
                    order_price.add(price_2[order_num - 1]);
                    System.out.println("Added " + menu_2[order_num - 1] + " to their order.");
                    System.out.println("Their order: " + order);
                    System.out.println("Their order price: " + order_price);
                    System.out.print("Ask how much do they want to buy.: ");
                    int quantity_item = Integer.parseInt(scanner.nextLine());
                    quantity.add(quantity_item);
                    break;
                } else {
                    System.out.println("Invalid input. Please try again.");
                }
            }
            while (true) {
                System.out.print("Ask if they would like to order more from this menu? (type y for yes / type n for no): ");
                String choice = scanner.nextLine();
                if (choice.equalsIgnoreCase("n")) {
                    break;
                } else if (choice.equalsIgnoreCase("y")) {
                    while (true) {
                        for (int i = 0; i < menu_2.length; i++) {
                System.out.println((i + 1) + "." + menu_2[i] + " - " + price_2[i]);
            }
                        System.out.print("Ask the customer what they would like to order (1-4): ");
                        int order_num = Integer.parseInt(scanner.nextLine());
                        if (order_num > 0 && order_num <= menu_2.length) {
                            order.add(menu_2[order_num - 1]);
                            order_price.add(price_2[order_num - 1]);
                            System.out.println("Added " + menu_2[order_num - 1] + " to their order.");
                            System.out.println("Their order: " + order);
                            System.out.println("Their order price: " + order_price);
                            System.out.print("Ask how much do they want to buy.: ");
                            int quantity_item = Integer.parseInt(scanner.nextLine());
                            quantity.add(quantity_item);
                            break;
                        } else {
                            System.out.println("Invalid input. Please try again.");
                        }
                    } 
                    continue;
                } else {
                    System.out.println("Invalid input. Please try again.");
                    continue;
                }
            }
            
        } else if (selection_num.equals("3")) {

            while (true) {
                            for (int i = 0; i < menu_3.length; i++) {
                System.out.println((i + 1) + "." + menu_3[i] + " - " + price_3[i]);
            }
                System.out.print("Ask the customer what they would like to order (1-3): ");
                int order_num = Integer.parseInt(scanner.nextLine());
                if (order_num > 0 && order_num <= menu_3.length) {
                    order.add(menu_3[order_num - 1]);
                    order_price.add(price_3[order_num - 1]);
                    System.out.println("Added " + menu_3[order_num - 1] + " to their order.");
                    System.out.println("Their order: " + order);
                    System.out.println("Their order price: " + order_price);
                    System.out.print("Ask how much do they want to buy.: ");
                    int quantity_item = Integer.parseInt(scanner.nextLine());
                    quantity.add(quantity_item);
                    break;
                } else {
                    System.out.println("Invalid input. Please try again.");
                }
            }
            while (true) {
                System.out.print("Ask if they would like to order more from this menu? (type y for yes / type n for no): ");
                String choice = scanner.nextLine();
                if (choice.equalsIgnoreCase("n")) {
                    break;
                } else if (choice.equalsIgnoreCase("y")) {
                    while (true) {
                                    for (int i = 0; i < menu_3.length; i++) {
                System.out.println((i + 1) + "." + menu_3[i] + " - " + price_3[i]);
            }
                        System.out.print("Ask the customer what they would like to order (1-3): ");
                        int order_num = Integer.parseInt(scanner.nextLine());
                        if (order_num > 0 && order_num <= menu_3.length) {
                            order.add(menu_3[order_num - 1]);
                            order_price.add(price_3[order_num - 1]);
                            System.out.println("Added " + menu_3[order_num - 1] + " to their order.");
                            System.out.println("Their order: " + order);
                            System.out.println("Their order price: " + order_price);
                            System.out.print("Ask how much do they want to buy.: ");
                            int quantity_item = Integer.parseInt(scanner.nextLine());
                            quantity.add(quantity_item);
                            break;
                        } else {
                            System.out.println("Invalid input. Please try again.");
                        }
                    } 
                    continue;
                } else {
                    System.out.println("Invalid input. Please try again.");
                    continue;
                }
            }
            
        } else if (selection_num.equals("4")) {
            break;
        } else {
            System.out.println("Menu doesn't exist.");
        }
    }
    
    double total = 0;

    for (int i = 0; i < order.size(); i++) {
        total += quantity.get(i) * order_price.get(i);
    }
    for (int i = 0; i < order.size(); i++) {
        System.out.printf("\n%d %s for %.2f each", quantity.get(i), order.get(i), order_price.get(i));
    }
    System.out.println("");
    System.out.println("The total amount will be " + total);

int money = 0;
while (true) {
System.out.print("Enter Payment: ");
money = Integer.parseInt(scanner.nextLine());
if (money < total) {
System.out.println("Money not enough");
} else {
System.out.println("Money is enough");
break;
}
}

double vat = total * 0.12; // calculate 12% VAT
double total_with_vat = total + vat; // add VAT to the total

double change = money - total_with_vat;

LocalDateTime now = LocalDateTime.now();
DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
String dt_string = dtf.format(now);

System.out.println("");
for (int i = 0; i < 80; i++) {
System.out.print("-");
}
System.out.println("\nCUSTOMER COPY");
System.out.println("Cashier: " + username);
for (int i = 0; i < 80; i++) {
System.out.print("-");
}
System.out.println("\n" + dt_string);
for (int i = 0; i < 80; i++) {
System.out.print("-");
}
for (int i = 0; i < order.size(); i++) {
System.out.printf("\n%d %s for %.2f each", quantity.get(i), order.get(i), order_price.get(i));
}

System.out.println("\n\nSubtotal: " + total);
System.out.println("VAT (12%): " + vat);
System.out.println("Total: " + total_with_vat);

System.out.println("\nYour change is: " + change);

for (int i = 0; i < 80; i++) {
System.out.print("*");
}
}
}

/* Mar Louis Go */
/* Kenneth Zarate */
/* Emmanuel Panong */
/*C Jay Macuse */
