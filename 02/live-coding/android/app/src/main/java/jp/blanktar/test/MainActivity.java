package jp.blanktar.test;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;
import android.view.View;


public class MainActivity extends AppCompatActivity{
	int count;

	@Override
	protected void onCreate(Bundle savedInstanceState){
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		count = 0;
		
		((TextView)findViewById(R.id.viewLabel)).setText("hello world".toCharArray(), 0, 11);
		
		findViewById(R.id.countup).setOnClickListener(new View.OnClickListener(){
			public void onClick(View view){
				count++;
				String text = count + "";
				((TextView)findViewById(R.id.viewLabel)).setText(text.toCharArray(), 0, text.length());
			}
		});
	}
}
