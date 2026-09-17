/**
 * Enumerate all iso classes of tournaments on n nodes, count how many are
 * strongly connected AND score-uniquely-determined (SC-SUD).
 *
 * Approach: enumerate labeled tournaments by score sequence, canonicalize each
 * via bucketed vertex permutations, dedupe, group by score. An iso class is
 * score-uniquely-determined iff it is alone in its score group.
 *
 * A tournament on n vertices is represented as a long adjacency bitmask
 * indexed by (i * n + j).
 */
import java.util.*;

public class TournamentEnum {
    static int n;
    static int E;
    static int[][] edges;    // (i, j) pairs with i < j

    public static void main(String[] args) {
        n = Integer.parseInt(args[0]);
        E = n * (n - 1) / 2;
        edges = new int[E][2];
        int idx = 0;
        for (int i = 0; i < n; i++) for (int j = i+1; j < n; j++) { edges[idx][0]=i; edges[idx][1]=j; idx++; }

        long start = System.currentTimeMillis();
        List<int[]> scores = enumerateScoreSequences();
        System.out.println("valid score sequences on n=" + n + ": " + scores.size());

        int totalIso = 0, sudIso = 0, scSud = 0, nonScSud = 0;
        long dedupeTime = 0;
        for (int[] s : scores) {
            long ts = System.currentTimeMillis();
            List<long[]> reps = classesForScore(s);
            dedupeTime += System.currentTimeMillis() - ts;
            totalIso += reps.size();
            boolean unique = reps.size() == 1;
            for (long[] pair : reps) {
                long adj = pair[0];
                boolean sc = pair[1] == 1L;
                if (unique) {
                    sudIso++;
                    if (sc) scSud++; else nonScSud++;
                }
            }
            System.out.printf("  score %s: %d iso classes  (%.1fs elapsed)%n",
                Arrays.toString(s), reps.size(), (System.currentTimeMillis()-start)/1000.0);
        }
        System.out.println();
        System.out.println("Total iso classes on n=" + n + ": " + totalIso);
        System.out.println("Score-uniquely-determined (SUD): " + sudIso);
        System.out.println("Strongly-connected AND SUD (SC-SUD): " + scSud);
        System.out.println("Non-SC SUD: " + nonScSud);
        System.out.printf("Total time: %.1fs%n", (System.currentTimeMillis()-start)/1000.0);
    }

    // --- Score sequence enumeration ---
    static List<int[]> enumerateScoreSequences() {
        List<int[]> out = new ArrayList<>();
        int total = n * (n - 1) / 2;
        int[] prefix = new int[n];
        scoreRec(out, prefix, 0, total, 0);
        return out;
    }

    static void scoreRec(List<int[]> out, int[] prefix, int idx, int remain, int minVal) {
        if (idx == n) {
            if (remain == 0) {
                int sum = 0;
                for (int i = 0; i < n; i++) {
                    sum += prefix[i];
                    if (sum < i*(i+1)/2) return;
                }
                out.add(prefix.clone());
            }
            return;
        }
        int maxVal = Math.min(n - 1, remain);
        for (int v = minVal; v <= maxVal; v++) {
            prefix[idx] = v;
            scoreRec(out, prefix, idx + 1, remain - v, v);
        }
    }

    // --- Realizer enumeration for a fixed score sequence ---
    static List<long[]> classesForScore(int[] scores) {
        // Iterate over 2^E orientations, filter to matching scores, canonicalize, dedupe.
        HashSet<Long> seenCanons = new HashSet<>();
        List<long[]> out = new ArrayList<>();
        // group vertices by target score for canonicalization buckets
        // Since scores is sorted ascending, vertex i has target scores[i]
        // Score groups: contiguous run of same value
        int[][] groups = groupsFromScores(scores);
        long limit = 1L << E;
        int[] deg = new int[n];
        for (long bits = 0; bits < limit; bits++) {
            // compute out-degrees
            Arrays.fill(deg, 0);
            for (int e = 0; e < E; e++) {
                if (((bits >> e) & 1) == 1) deg[edges[e][0]]++;
                else deg[edges[e][1]]++;
            }
            // match sorted deg to scores
            boolean match = true;
            for (int i = 0; i < n; i++) if (deg[i] != scores[i]) { match = false; break; }
            if (!match) continue;
            // build adjacency
            long adj = 0L;
            for (int e = 0; e < E; e++) {
                int a = edges[e][0], b = edges[e][1];
                if (((bits >> e) & 1) == 1) adj |= 1L << (a * n + b);
                else adj |= 1L << (b * n + a);
            }
            long canon = canonicalize(adj, groups);
            if (seenCanons.add(canon)) {
                boolean sc = isStronglyConnected(canon);
                out.add(new long[]{canon, sc ? 1L : 0L});
            }
        }
        return out;
    }

    static int[][] groupsFromScores(int[] scores) {
        List<int[]> gs = new ArrayList<>();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && scores[j] == scores[i]) j++;
            int[] g = new int[j - i];
            for (int k = 0; k < g.length; k++) g[k] = i + k;
            gs.add(g);
            i = j;
        }
        return gs.toArray(new int[0][]);
    }

    static long canonicalize(long adj, int[][] groups) {
        // Try all permutations respecting score-buckets. Return lex-min adjacency mask.
        int[] order = new int[n];
        long[] best = new long[]{Long.MAX_VALUE};
        int[][] gsCopy = new int[groups.length][];
        for (int i = 0; i < groups.length; i++) gsCopy[i] = groups[i].clone();
        permuteRec(adj, gsCopy, 0, order, best);
        return best[0];
    }

    static void permuteRec(long adj, int[][] groups, int gIdx, int[] order, long[] best) {
        if (gIdx == groups.length) {
            long relabeled = 0L;
            for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) {
                if (((adj >> (order[i] * n + order[j])) & 1L) == 1L) relabeled |= 1L << (i * n + j);
            }
            if (relabeled < best[0]) best[0] = relabeled;
            return;
        }
        int[] g = groups[gIdx];
        int gStart = 0;
        for (int i = 0; i < gIdx; i++) gStart += groups[i].length;
        permute(g, 0, adj, groups, gIdx, order, gStart, best);
    }

    static void permute(int[] g, int start, long adj, int[][] groups, int gIdx, int[] order, int oStart, long[] best) {
        if (start == g.length) {
            for (int i = 0; i < g.length; i++) order[oStart + i] = g[i];
            permuteRec(adj, groups, gIdx + 1, order, best);
            return;
        }
        for (int i = start; i < g.length; i++) {
            int tmp = g[start]; g[start] = g[i]; g[i] = tmp;
            permute(g, start + 1, adj, groups, gIdx, order, oStart, best);
            tmp = g[start]; g[start] = g[i]; g[i] = tmp;
        }
    }

    static boolean isStronglyConnected(long adj) {
        // forward reachability from 0
        int f = reach(adj, 0, false);
        int b = reach(adj, 0, true);
        int all = (1 << n) - 1;
        return f == all && b == all;
    }

    static int reach(long adj, int start, boolean reverse) {
        int seen = 1 << start;
        int frontier = 1 << start;
        while (frontier != 0) {
            int next = 0;
            for (int u = 0; u < n; u++) {
                if (((frontier >> u) & 1) == 0) continue;
                for (int v = 0; v < n; v++) {
                    if (((seen >> v) & 1) != 0) continue;
                    long bit = reverse ? (1L << (v * n + u)) : (1L << (u * n + v));
                    if ((adj & bit) != 0) next |= 1 << v;
                }
            }
            seen |= next;
            frontier = next;
        }
        return seen;
    }
}
