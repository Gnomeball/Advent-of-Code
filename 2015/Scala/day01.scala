import scala.io.Source
import scala.util.Using

object day01 {

  def partOne(directions: List[Char]): Int = {
    directions.map {
      case '(' => 1
      case ')' => -1
    }.sum
  }

  def partTwo(directions: List[Char]): Int = {
    directions.map {
      case '(' => 1
      case ')' => -1
    }.scanLeft(0)(_ + _).indexWhere(_ < 0)
  }

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day01.txt"
    val brackets = Using.resource(Source.fromFile(inputFile)) { source =>
      source.mkString.toList
    }

    println(partOne(brackets))
    println(partTwo(brackets))
  }
}
