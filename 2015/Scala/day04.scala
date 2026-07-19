import scala.io.Source
import scala.util.Using
import java.security.MessageDigest
import scala.annotation.tailrec

object day04 {

  private def findNumber(digest: String, zeroes: Int): Int = {
    val prefix = "0" * zeroes

    def md5Hex(s: String): String = {
      val digest = MessageDigest.getInstance("MD5").digest(s.getBytes("UTF-8"))
      digest.map(b => f"$b%02x").mkString
    }

    @tailrec
    def findNumberWithLeadingZeros(number: Int): Int = {
      val hash = md5Hex(digest + number)
      if (hash.startsWith(prefix)) number
      else findNumberWithLeadingZeros(number + 1)
    }

    findNumberWithLeadingZeros(100000)
  }

  def partOne(input: String): Int = findNumber(input, 5)
  def partTwo(input: String): Int = findNumber(input, 6)

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day04.txt"

    val digest = Using.resource(Source.fromFile(inputFile)) { source =>
      source.mkString
    }

    println(partOne(digest))
    println(partTwo(digest))
  }

}
