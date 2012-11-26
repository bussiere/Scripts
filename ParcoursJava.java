import java.io.File;
import java.util.ArrayList;

public class ParcoursJava
{

    



    private static ArrayList<String> listDirectory(String dir)
    {
        
        ArrayList<String> listefichier = new ArrayList();
         int filecount = 0;

         int dircount = 0;
        File file = new File(dir);
        File[] files = file.listFiles();
        if (files != null)
        {
            for (int i = 0; i < files.length; i++)
            {
                if (files[i].isDirectory() == true)
                {
                    System.out.println("Dossier" + files[i].getAbsolutePath());
                   dircount++;
                }
                else
                {
                    System.out.println("Fichier" + files[i].getName());
                    filecount++;
                    listefichier.add(files[i].getAbsolutePath());
                    
                }
                if (files[i].isDirectory() == true)
                {
                    listefichier.addAll(listDirectory(files[i].getAbsolutePath()));
                }

            }
        }
        return listefichier;

    }

    public static void main(String[] args)
    {
        String pathToExplore = "C:\\AtelierSODA\\workspaceSODA\\madrhas\\";
        System.out.println("test");
        ArrayList<String> listefichier = listDirectory(pathToExplore);
        
       for (String fichier : listefichier)
       {
           System.out.println(fichier);
       }
    }

}
