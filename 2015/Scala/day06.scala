import scala.io.Source
import scala.util.Using

object day06 {

  def partOne(instructions: List[(Int, Array[Int], Array[Int])]): Int = {
    val grid = Array.fill(1000, 1000)(-1) // initialise to -1 (off)

    instructions.foreach { case (state, fromCoords, toCoords) =>
      for x <- fromCoords(0) to toCoords(0)
          y <- fromCoords(1) to toCoords(1) do
        state match
          case  1 => grid(x)(y)  =  1 // on
          case -1 => grid(x)(y)  = -1 // off
          case  0 => grid(x)(y) *= -1 // toggle
    }

    // Return count of how many lights are now on
    grid.flatten.count(_ > 0)
  }

  def partTwo(instructions: List[(Int, Array[Int], Array[Int])]): Int = {
    val grid = Array.fill(1000, 1000)(0) // initialise to 0 brightness

    instructions.foreach { case (state, fromCoords, toCoords) =>
      for x <- fromCoords(0) to toCoords(0)
          y <- fromCoords(1) to toCoords(1) do
        state match
          case  1 => grid(x)(y) += 1 // up
          case -1 => grid(x)(y)  = math.max(grid(x)(y) - 1, 0) // down
          case  0 => grid(x)(y) += 2 // up 2
    }

    // Return total brightness
    grid.flatten.sum
  }

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day06.txt"

    val instructions = Using.resource(Source.fromFile(inputFile)) { source =>
      val splitCoords = (c: String) => c.split(",").map(_.toInt)
      source.getLines().map(line => {
        val words = line.split(" ")
        if words.size == 5 then {
          // turn on/off x,y through x,y
          val state = if words(1).equals("on") then 1 else -1
          (state, splitCoords(words(2)), splitCoords(words(4)))
        } else {
          // toggle x,y through x,y
          (0, splitCoords(words(1)), splitCoords(words(3)))
        }
      }).toList
    }

    println(partOne(instructions))
    println(partTwo(instructions))
  }

}
