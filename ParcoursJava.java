import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

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

    private static void AnalyseLigne(String ligne, String fichier, int numeroLigne)

    {
        try
        {
            Pattern p = Pattern.compile(".*(\\w[ \\t\\r\\n\\v\\f]((\\w\\w)|(\\w))[ \\t\\r\\n\\v\\f]).*[\\;|\\=].*");
            Matcher m = p.matcher(ligne);
            while (m.find())
            {
                System.out.println(ligne.substring(m.start(), m.end()));
                FileWriter writer;
                try
                {
                    writer = new FileWriter("output.txt", true);
                    writer.write(ligne + ":" + fichier + ":" + numeroLigne+"\r\n\r\n");
                    writer.close();
                }
                catch (IOException e)
                {
                }   
            }

           

        }
        catch (PatternSyntaxException pse)
        {
        }
    }

    private static void AnalyseFichier(String fichier)
    {
        int i = 0;
        Scanner scanner;
        try
        {
            scanner = new Scanner(new FileReader(fichier));
            String str = null;
            while (scanner.hasNextLine())
            {
                str = scanner.nextLine();
                System.out.println(str);
                AnalyseLigne(str, fichier, i);
                i++;

            }
        }
        catch (FileNotFoundException e)
        {
            scanner = null;
        }

    }

    public static void main(String[] args)
    {
        String pathToExplore = "C:\\AtelierSODA\\workspaceSODA\\madrhas\\";
        System.out.println("test");
        ArrayList<String> listefichier = listDirectory(pathToExplore);

        for (String fichier : listefichier)
        {

            if (fichier.matches(".*\\.java$"))
            {
                System.out.println(fichier);
                AnalyseFichier(fichier);
            }
        }
    }

}
