package com.slowfrog.qwop.ui;

import java.awt.Robot;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.io.*;

import com.slowfrog.qwop.ConsoleLog;
import com.slowfrog.qwop.Log;
import com.slowfrog.qwop.Qwopper;
import com.slowfrog.qwop.RunInfo;

public class Main {

  private static final Log LOG = new ConsoleLog();
  private static Robot rob;
  private static Qwopper qwop;

  public static void main(String[] args) {

    int tries = 10;
    int count = 1;
    String str = null;
    if (args.length > 0) {
      try {
        tries = Integer.parseInt(args[0]);
        if (args.length > 1) {
          count = Integer.parseInt(args[1]);
        }

      } catch (NumberFormatException e) {
        // First arg is not a number: probably a code string
        str = args[0];
      }
    }


    try {
      rob = new Robot();
      qwop = new Qwopper(rob, LOG);
      qwop.findRealOrigin();

    } catch (Throwable t) {
      LOG.log("Error", t);
    }
  }

  public static RunInfo playOneGame(String str)
  {
    RunInfo info;
    try {
      qwop.findRealOrigin();
    } catch (Throwable t) {
      LOG.log("Error", t);
    }
    qwop.startGame();
    info = qwop.playOneGame(str, 60000);
    return info;
  }

  private static void testString(Qwopper qwop, String str, int count, int round) {
    for (int i = 0; i < count; ++i) {
      LOG.logf("Run #%d.%d\n", round, i);
      qwop.startGame();
      RunInfo info = qwop.playOneGame(str, 60000);
      LOG.log(info.toString());
      LOG.log(info.marshal());
      saveRunInfo("runs.txt", info);
    }
  }

  private static void saveRunInfo(String filename, RunInfo info) {
    try {
      PrintStream out = new PrintStream(new FileOutputStream(filename, true));
      try {
        out.println(info.marshal());
      } finally {
        out.flush();
        out.close();
      }
    } catch (IOException ioe) {
      LOG.log("Error marshalling", ioe);
    }
  }

}
