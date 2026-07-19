import scala.io.Source
import scala.util.Using

object day07 {

  /**
   * Represent an abstract syntax tree for logical expressions.
   *
   * The possible subtypes include:
   * - Wire   : a named wire in the circuit
   * - Value  : a constant integer value
   * - Not    : a logical "NOT" against a wire
   * - And    : a logical "AND" between two wires
   * - Or     : a logical "OR" between two wires
   * - LShift : a logical left shift operation on a wire by a specified amount
   * - RShift : a logical right shift operation on a wire by a specified amount
   */
  sealed trait Expr
  private case class Wire(name: String) extends Expr
  private case class Value(n: Int) extends Expr
  private case class Not(in: Expr) extends Expr
  private case class And(left: Expr, right: Expr) extends Expr
  private case class Or(left: Expr, right: Expr) extends Expr
  private case class LShift(left: Expr, amount: Int) extends Expr
  private case class RShift(left: Expr, amount: Int) extends Expr

  /**
   * Parses a line of input into a wire name and an expression.
   *
   * @param line The input line to parse.
   * @return A tuple containing the wire name and the corresponding expression.
   */
  private def parseLine(line: String): (String, Expr) = {
    def parseExpr(parts: Array[String]): Expr = {
      def operand(token: String): Expr =
        if token.forall(_.isDigit)
        then Value(token.toInt) else Wire(token)

      parts match
        case Array(single) =>
          operand(single)
        case Array("NOT", in) =>
          Not(operand(in))
        case Array(left, "AND", right) =>
          And(operand(left), operand(right))
        case Array(left, "OR", right) =>
          Or(operand(left), operand(right))
        case Array(left, "LSHIFT", amount) =>
          LShift(operand(left), amount.toInt)
        case Array(left, "RSHIFT", amount) =>
          RShift(operand(left), amount.toInt)
        // case _ => // Unreachable
    }

    // Return the right as the key, and the parsed expression as the value
    val Array(left, right) = line.split(" -> ")
    right -> parseExpr(left.split("\\s+"))
  }

  /**
   * Resolves the value of an expression within the circuit.
   *
   * @param expr The expression to resolve.
   * @param circuit The circuit containing the expressions.
   * @param cache A mutable map to cache resolved values.
   * @return The resolved value of the expression.
   */
  private def resolve(expr: Expr, circuit: Map[String, Expr],
                      cache: scala.collection.mutable.Map[String, Int]): Int = {
    // for each wire, recursively attempt to resolve its value
    expr match
      case Value(n) => // return the value directly
        n
      case Wire(name) => // we may have already resolved this?
        cache.getOrElseUpdate(name, resolve(circuit(name), circuit, cache))
      case Not(in) =>
        (~resolve(in, circuit, cache))
      case And(left, right) =>
        (resolve(left, circuit, cache) & resolve(right, circuit, cache))
      case Or(left, right) =>
        (resolve(left, circuit, cache) | resolve(right, circuit, cache))
      case LShift(left, amount) =>
        (resolve(left, circuit, cache) << amount)
      case RShift(left, amount) =>
        (resolve(left, circuit, cache) >>> amount)
  }

  def partOne(circuit: Map[String, Expr]): Int =
    val cache = scala.collection.mutable.Map.empty[String, Int]
    resolve(Wire("a"), circuit, cache)

  def partTwo(circuit: Map[String, Expr], b_override: Int): Int =
    val overriddenCircuit = circuit.updated("b", Value(b_override))
    val cache = scala.collection.mutable.Map.empty[String, Int]
    resolve(Wire("a"), overriddenCircuit, cache)

  def main(args: Array[String]): Unit = {
    val inputFile = "2015/data/day07.txt"

    val circuit = Using.resource(Source.fromFile(inputFile)) { source =>
      source.getLines().map(parseLine).toMap
    }

    // we need to re-use this for part two
    val p1 = partOne(circuit)

    println(p1)
    println(partTwo(circuit, p1))
  }

}
