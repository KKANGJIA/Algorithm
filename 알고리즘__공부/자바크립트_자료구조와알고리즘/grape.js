// 그래프 알고리즘 코드 (IIFE 사용하는 이유: 비공개 변수를 만들기 위함, 클래스로 설정하는 것과 같은 역할)
var Graph = (function() {
    function Vertex(key) {
      this.next = null;
      this.arc = null;
      this.key = key;
      this.inTree = null;
    }
    function Arc(data, dest, capacity) {
      this.nextArc = null;
      this.destination = dest;
      this.data = data;
      this.capacity = capacity;
      this.inTree = null;
    }
    function Graph() {
      this.count = 0;
      this.first = null;
    }
    Graph.prototype.insertVertex = function(key) {
      var vertex = new Vertex(key);
      var last = this.first;
      if (last) {
        while (last.next !== null) {
          last = last.next;
        }
        last.next = vertex;
      } else {
        this.first = vertex;
      }
      this.count++;
    };
    Graph.prototype.deleteVertex = function(key) {
      var vertex = this.first;
      var prev = null;
      while (vertex.key !== key) {
        prev = vertex;
        vertex = vertex.next;
      }
      if (!vertex) return false;
      if (!vertex.arc) return false;
      if (prev) {
        prev.next = vertex.next;
      } else {
        this.first = vertex.next;
      }
      this.count--;
    };
    Graph.prototype.insertArc = function(data, fromKey, toKey, capacity) {
      var from = this.first;
      var to = this.first;
      while (from && from.key !== fromKey) {
        from = from.next;
      }
      while (to && to.key !== toKey) {
        to = to.next;
      }
      if (!from || !to) return false;
      var arc = new Arc(data, to, capacity);
      var fromLast = from.arc;
      if (fromLast) {
        while (fromLast.nextArc != null) {
          fromLast = fromLast.nextArc;
        }
        fromLast.nextArc = arc;
      } else {
        from.arc = arc;
      }
    };
    Graph.prototype.deleteArc = function(fromKey, toKey) {
      var from = this.first;
      while (from !== null) {
        if (from.key === fromKey) break;
        from = from.next;
      }
      if (!from) return false;
      var fromArc = from.arc;
      var preArc;
      while (fromArc !== null) {
        if (toKey === fromArc.destination.key) break;
        preArc = fromArc;
        fromArc = fromArc.next;
      }
      if (!fromArc) return false;
      if (preArc) {
        preArc.nextArc = fromArc.nextArc;
      } else {
        from.arc = fromArc.nextArc;
      }
    };
    return Graph;
  })();
  
  // 실행
  var graph = new Graph();
  graph.insertVertex('A');
  graph.insertVertex('B');
  graph.insertVertex('C');
  graph.insertVertex('D');
  graph.insertVertex('E');
  graph.insertVertex('F');
  graph.insertArc(1, 'A', 'B');
  graph.insertArc(1, 'B', 'C');
  graph.insertArc(1, 'B', 'E');
  graph.insertArc(1, 'C', 'E');
  graph.insertArc(1, 'C', 'D');
  graph.insertArc(1, 'E', 'D');
  graph.insertArc(1, 'E', 'F');

  // Vertex는 Vertex끼리 연결리스트를 취하고 있고, 각각의 Vertex는 자신과 연결된 Arc에 대한 연결리스트도 가지고 있습니다. 
  // 위의 그래프는 방향 그래프이기 때문에 한쪽 방향으로만 연결되어 있습니다. 