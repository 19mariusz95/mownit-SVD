package crawler;

import edu.uci.ics.crawler4j.crawler.Page;
import edu.uci.ics.crawler4j.crawler.WebCrawler;
import edu.uci.ics.crawler4j.parser.HtmlParseData;
import edu.uci.ics.crawler4j.parser.ParseData;
import edu.uci.ics.crawler4j.url.WebURL;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.regex.Pattern;

/**
 * Created by Mariusz on 01.05.2016.
 */
public class MyCrawler extends WebCrawler {
    private Pattern filters = Pattern.compile(".*(\\.(css|js|gif|jpg" + "|png|mp3|mp3|zip|gz))$");
    private Set<Document> pagestext = new HashSet<>();

    @Override
    public void visit(Page page) {
        String url = page.getWebURL().getURL();
        ParseData htmlParseData = page.getParseData();
        if (htmlParseData instanceof HtmlParseData) {
            System.out.println("URL: " + url);
            String text = ((HtmlParseData) htmlParseData).getText();
            Map<String, Integer> map = new HashMap<>();
            String[] array = text.toLowerCase().split(" ");
            for (String s : array) {
                String tmp = s.trim();
                if (tmp.matches("^[a-z]*")) {
                    MainClass.set.add(tmp);
                    if (!map.containsKey(tmp)) {
                        map.put(tmp, 1);
                    } else {
                        map.put(tmp, map.get(tmp) + 1);
                    }
                }
            }
            Document document = new Document(url, map);
            pagestext.add(document);
        }
    }

    @Override
    public boolean shouldVisit(Page referringPage, WebURL url) {
        String href = url.getURL().toLowerCase();
        return !filters.matcher(href).matches() && href.startsWith("https://en.wikipedia.org/wiki");
    }

    @Override
    public Object getMyLocalData() {
        return pagestext;
    }
}
