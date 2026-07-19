import scala.io.Source
import scala.util.Using

object day05 {

  def partOne(strings: List[String]): Int = {
    def stringIsNice(s: String): Boolean = {
      val vowels = s.count(Set('a', 'e', 'i', 'o', 'u').contains)
      val doubleLetter = s.sliding(2).exists(_.distinct.length == 1)
      val forbidden = s.contains("ab") || s.contains("cd") || s.contains("pq") || s.contains("xy")
      vowels >= 3 && doubleLetter && !forbidden
    }

    strings.count(stringIsNice)
  }

  def partTwo(strings: List[String]): Int = {
    def stringIsNice(s: String): Boolean = {
      val doublePair = s.indices.dropRight(1).exists { i =>
        val pair = s.substring(i, i + 2)
        s.indexOf(pair, i + 2) != -1
      }
      val repeatLetter = s.sliding(3).exists(chunk => chunk(0) == chunk(2))
      doublePair && repeatLetter
    }

    strings.count(stringIsNice)
  }

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day05.txt"

    val strings = Using.resource(Source.fromFile(inputFile)) { source =>
      source.getLines().toList
    }

    println(partOne(strings))
    println(partTwo(strings))
  }

}
