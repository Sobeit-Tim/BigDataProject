import org.apache.spark.graphx.GraphLoader
import java.io._

val graph = GraphLoader.edgeListFile(sc, "edges.txt")

val ranks = graph.pageRank(0.0001).vertices
ranks.foreach(println)

val swappedRanks = ranks.map(_.swap)

val sortedRanks = swappedRanks.sortByKey(false)


val pw = new PrintWriter(new File("result.txt"))


for(pr_node <- sortedRanks.collect().take(5)){
    pw.write(pr_node.toString)
    pw.println("")
    }



pw.close()
sc.stop()


