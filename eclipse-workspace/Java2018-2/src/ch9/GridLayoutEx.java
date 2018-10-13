package ch9;

import java.awt.GridLayout;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class GridLayoutEx extends JFrame {
	public GridLayoutEx() {
		// TODO Auto-generated constructor stub
		setTitle("GridLayout Sample");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		GridLayout grid = new GridLayout(4,2);
		
		grid.setVgap(5);
		setLayout(grid);
		add(new JLabel("�̸�"));
		add(new JTextField(""));
		add(new JLabel("�й�"));
		add(new JTextField(""));
		add(new JLabel("�а�"));
		add(new JTextField(""));
		add(new JLabel("����"));
		add(new JTextField(""));
		
		setSize(300,200);
		setVisible(true);
	}
	public static void main(String[] args) {
		new GridLayoutEx();
	}
}