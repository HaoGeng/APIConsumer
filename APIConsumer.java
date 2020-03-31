import java.util.*;

public class APIConsumer {

    public static void main (String[] args) {
        System.out.println(selectOperation());
    }

    public enum Operations {
        LIST_TITLES_POSTS,
        PRINT_EMAIL_UID,
        CREATE_POST_PRINT_PID,
        LIST_TITLES_POSTS_UID,
        UPDATE_POST
    }

    // select operation
    public static Operations selectOperation () {
        Scanner inputScanner = new Scanner(System.in);
        String input = null;

        List<String> options = Arrays.asList("1", "2", "3", "4", "5");

        // request Operation until user input a correct one
        do {
            if (input != null) {
                System.out.println("Invalid input, please enter again: ");
            }
            else {
                System.out.println("Required operations: \n" + 
                                    "1. List all the titles of all posts. \n" + 
                                    "2. Print the email of the user with id # 5. \n" + 
                                    "3. Create a new post and print the id of the created post. \n" + 
                                    "4. List the titles of all the posts created by user 5. \n" + 
                                    "5. Update post # 14 with a new title \"I passed the test!\". Print the response of that request.");
                System.out.println("Please enter an integer for the operation: ");
            }

            input = inputScanner.next();
        } while (!options.contains(input));

        inputScanner.close();

        int operationIndex = Integer.parseInt(input);

        return Operations.values()[operationIndex-1];
    }
}