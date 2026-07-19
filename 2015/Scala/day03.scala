import scala.io.Source
import scala.util.Using

object day03 {

  private def walk(moves: List[Char]): Set[(Int, Int)] = {
    var seen = Set[(Int, Int)]((0, 0))
    var position = (0, 0)

    def delta(direction: Char): (Int, Int) = {
      direction match {
        case '^' => (0, 1)
        case 'v' => (0, -1)
        case '<' => (-1, 0)
        case '>' => (1, 0)
      }
    }

    for direction <- moves do {
      val (dx, dy) = delta(direction)
      position = (position._1 + dx, position._2 + dy)
      seen += position
    }

    seen
  }

  def partOne(directions: List[Char]): Int = {
    walk(directions).size
  }

  def partTwo(directions: List[Char]): Int = {
    val santaMoves = directions.zipWithIndex.collect { case (d, i) if i % 2 == 0 => d }
    val roboMoves = directions.zipWithIndex.collect { case (d, i) if i % 2 == 1 => d }
    (walk(santaMoves) union walk(roboMoves)).size
  }

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day03.txt"

    val directions = Using.resource(Source.fromFile(inputFile)) { source =>
      source.mkString.toList
    }

    println(partOne(directions))
    println(partTwo(directions))
  }

}
