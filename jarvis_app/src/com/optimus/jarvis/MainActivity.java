package com.optimus.jarvis;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebSettings;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        WebView webView = new WebView(this);
        WebSettings webSettings = webView.getSettings();
        webSettings.setJavaScriptEnabled(true);
        webView.setWebViewClient(new WebViewClient());
        // यह सीधे आपके बैकग्राउंड में चल रहे पायथन कर्नल से डेटा सिंक करेगा
        webView.loadUrl("http://127.0.0.1:5000");
        setContentView(webView);
    }
}
