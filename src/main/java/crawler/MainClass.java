package crawler;

import edu.uci.ics.crawler4j.crawler.CrawlConfig;
import edu.uci.ics.crawler4j.crawler.CrawlController;
import edu.uci.ics.crawler4j.fetcher.PageFetcher;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtConfig;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtServer;

import java.io.File;
import java.io.FileOutputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by Mariusz on 01.05.2016.
 */
public class MainClass {
    public static Set<String> set = new HashSet<String>();

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(args[0]);
        int numberofcrawlers = 8;
        CrawlConfig config = new CrawlConfig();
        config.setMaxPagesToFetch(n);
        config.setCrawlStorageFolder("/data/crawl/root");

        PageFetcher pageFetcher = new PageFetcher(config);
        RobotstxtConfig robotstxtConfig = new RobotstxtConfig();
        RobotstxtServer robotstxtServer = new RobotstxtServer(robotstxtConfig, pageFetcher);
        CrawlController crawlController = new CrawlController(config, pageFetcher, robotstxtServer);

        crawlController.addSeed("https://en.wikipedia.org/");
        crawlController.start(MyCrawler.class, numberofcrawlers);

        crawlController.waitUntilFinish();

        List<Object> crawlersLocalData = crawlController.getCrawlersLocalData();
        List<Document> documents = new ArrayList<Document>();
        crawlersLocalData.forEach(f -> {
            Set<Document> set = (Set<Document>) f;
            set.forEach(documents::add);
        });

        File file = new File("data.txt");
        PrintWriter pw = new PrintWriter(new FileOutputStream(file), false);
        pw.println(documents.size());
        documents.forEach(f -> pw.println(f.getURL()));
        pw.println(set.size());
        for (String term : set) {
            pw.print(term + " ");
            for (Document doc : documents) {
                pw.print(doc.getMap().getOrDefault(term, 0) + " ");
            }
            pw.println();
        }
        pw.flush();
        pw.close();
        System.out.println("saved " + file.getAbsolutePath());
    }
}
