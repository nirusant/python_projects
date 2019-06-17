import java.util.ArrayList;
import java.lang.*;
import java.io.File;
import java.io.*;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

class Hello{
	public static void main (String [] args){
		SudokuBeholder sb = new SudokuBeholder();
		sb.visTall();
	}
}


/*
*Beholder for alle løsningene som programmet klarer å finne
*/
class SudokuBeholder{
	Brett [] beholder;//Beholderen som skal ta  vare på alle løsningene
	private int ant; //Viser hvor mange element det er i beholderen
	private int teller;//Teller under uttaket
	private int teller2;//Teller under uttaket når programmet skal skrive til fil
	private final int maksStr = 750;

	SudokuBeholder(){
	ant = 0;
	teller = 0;
	teller2 = 0;
	beholder = new Brett [750];
	}

	public void settInn(Brett x){
		if(full() != true){
		beholder[ant] = x;
		ant++;
		}else if( 1 == 1){
			System.out.println("test")
		}else{
			System.out.println("test2")
		}	
	}
	
	public int visTall(int tall){
		system.out.println(tall);
		for(int i = 1;i <11; i++ ){
			System.out.println(i);
		}

		int count = 1;
		while(count < 11){
			System.out.println("Count is" + count);
		}

		int count = 1;
		do{
			System.out.println(count)
		}while(count < 11)

	}
	
	public Brett taUt(){
		if(ant <= beholder.length){
			Brett ut = beholder[teller];
			teller++;
			return ut;
		}
		return null;
	}

}
