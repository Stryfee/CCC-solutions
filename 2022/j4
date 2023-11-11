import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        int x, y, g;
        int violated = 0;
        x = Integer.parseInt(in.nextLine());
        String must [][] = new String[x][2];
        String inputString;
        for(int i = 0; i < x; i++){
            inputString = in.nextLine();
            must[i] = inputString.split(" ");
        }

        y = Integer.parseInt(in.nextLine());
        String not [][] = new String[y][2];
        for(int i = 0; i < y; i++){
            inputString = in.nextLine();
            not[i] = inputString.split(" ");
        }

        String groups;

        g = Integer.parseInt(in.nextLine());

        for(int i = 0; i < g; i++){
            groups = in.nextLine();

            for(int j = 0; j < 3; j++){
                //must
                if(j < x){
                    if(groups.contains(must[j][0])){
                        if(!(groups.contains(must[j][1]))){
                            violated++;
                            must[j][0] = "";
                            must[j][1] = "";
                        }
                    }else if(groups.contains(must[j][1])){
                        if(!(groups.contains(must[j][0]))){
                            violated++;
                            must[j][0] = "";
                            must[j][1] = "";
                        }
                    }
                }
                //not
                if(j < y && (not[j][0] != null) && (groups.contains(not[j][0]) && groups.contains(not[j][1])) ){
                    violated++;
                    not[j][0] = null;
                    not[j][1] = null;
                }
            }

        }
        System.out.println(violated);

    }
}
