var LinkedList = (function() {
    function LinkedList() {
      this.length = 0;
      this.head = null;
    }
    function Node(data) {
      this.data = data;
      this.next = null;
    }
    return LinkedList;
  })();
  
  // LinkedList에는 length와 head가 있습니다. 
  // length는 노드의 개수를 표현하는 부분이고, head가 바로 첫 노드의 주소를 가리키는 부분입니다. 
  
  // 이제 데이터를 추가, 검색, 삭제하는 메소드를 구현해봅시다.
  var LinkedList = (function() {
    function LinkedList() {
      this.length = 0;
      this.head = null;
    }
    function Node(data) {
      this.data = data;
      this.next = null;
    }
    LinkedList.prototype.add = function(value) {
      var node = new Node(value);
      var current = this.head;
      if (!current) { // 현재 아무 노드도 없으면
        this.head = node; // head에 새 노드를 추가합니다.
        this.length++;
        return node;
      } else { // 이미 노드가 있으면
        while(current.next) { // 마지막 노드를 찾고.
          current = current.next;
        }
        current.next = node; // 마지막 위치에 노드를 추가합니다.
        this.length++;
        return node;
      }
    };
    //prototype으로 속성을 만들어서 LinkedList로 만드는 객체에 자동으로 추가할 수 있도록 프로토타입으로 설정
    LinkedList.prototype.search = function(position) { 
      var current = this.head;
      var count = 0;
      while (count < position) { // position 위치만큼 이동합니다.
        current = current.next;
        count++;
      }
      return current.data;
    };
    LinkedList.prototype.remove = function(position) {
      var current = this.head;
      var before;
      var remove;
      var count = 0;
      if (position == 0) { // 맨 처음 노드를 삭제하면
        remove= this.head;
        this.head = this.head.next; // head를 두 번째 노드로 교체
        this.length--;
        return remove;
      } else { // 그 외의 다른 노드를 삭제하면
        while (count < position) {
          before = current;
          count++;
          current = current.next;
        }
        remove = current;
        before.next = remove.next;
        // remove 메모리 정리
        this.length--;
        return remove;
      }
    };
    return LinkedList;
  })();
  
  // 물론 추가할 때는 굳이 마지막에 추가하지 않아도 되고, 중간에 끼워넣는다든지, 맨 처음에 끼워넣어도 되겠죠? 직접 구현해보세요. 

  // 실행
  var list = new LinkedList();
  list.add(1);
  list.add(2);
  list.add(3);
  list.length; // 3
  list.search(0); // 1
  list.search(2); // 3
  list.remove(1);
  list.length; // 2