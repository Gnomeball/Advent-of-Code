import scala.io.Source
import scala.util.Using

object day02 {

  def partOne(dimensions: List[(Int, Int, Int)]): Int = {
    dimensions.map { case (l, w, h) =>
      val Array(a, b, c) = Array(l * w, w * h, h * l).sorted
      2 * (a + b + c) + a
    }.sum
  }

  def partTwo(dimensions: List[(Int, Int, Int)]): Int = {
    dimensions.map { case (l, w, h) =>
      val Array(a, b, _) = Array(l, w, h).sorted
      2 * (a + b) + (l * w * h)
    }.sum
  }

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day02.txt"
    val dimensions = Using.resource(Source.fromFile(inputFile)) { source =>
      source.getLines().toList.map { line =>
        val Array(l, w, h) = line.split("x").map(_.toInt)
        (l, w, h)
      }
    }

    println(partOne(dimensions))
    println(partTwo(dimensions))
  }
}



