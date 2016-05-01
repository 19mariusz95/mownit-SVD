package crawler;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by Mariusz on 01.05.2016.
 */
public class Document {
    private String url;
    private Map<String, Integer> map = new HashMap<>();

    public Document(String url, Map<String, Integer> map) {
        this.url = url;
        this.map = map;
    }

    public String getURL() {
        return url;
    }

    public Map<String, Integer> getMap() {
        return map;
    }
}
