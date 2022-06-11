## 1. Simplicail Complex

> 📌 **핵심 Keyword**
> - **위상수학** : 거리나 좌표계의 개념에 의존하지 않고, 대상의 연결성에 대한 기하학적 특징을 다루는 수학.
> - **심플리셜 컴플렉스** : 꼭짓점과 변으로 연결성을 표현하는 그래프의 일반화된 개념. 꼭짓점, 변, 삼각형, 정사면체 등으로 고차원적인 연결성을 표현한다.
> - **필트레이션** : 심플리셜 컴플렉스의 진화과정을 표현한 서브컴플렉스들의 증가하는 배열.
> 




### §. 1.1.) Graph

**위상수학**(Topology)에서 관심있는것들 중 하나는 대상이 가진 **연결성**이라고 할 수 있습니다.
위상수학은 이러한 연결성을 표현하는 법과 연결성으로부터 얻어지는 기하학적 특징들을 계산하는 방법을 다루고 있습니다.
위상수학에 대해서는 그 이름처럼 봐도 봐도 *또모르지*.. 라는 유우머가 교수님들대부터 저희 세대까지 물려져온 만큼 깊게 다룰 생각은 없습니다.
개인적인 소견으로 TDA를 이해함에 있어서 "위상수학은 연결성을 다루고자 한다"는 철학만 마음으로 받아들인다면, 두꺼운 일반위상수학의 개론들을 하나 하나 다 이해할 필요는 없다고 생각합니다.
부득이 일반위상수학의 개념을 사용해야한다면, 글꼬리로 설명을 최대한 덧붙이도록 하겠습니다.

위상수학이 연결성을 다루고자 한다는 철학을 대표적으로 보여주는 예제가 **그래프**입니다.
**그래프**(Graph)도 꼭짓점(vertex)들과 그 꼭짓점들을 연결하는 변(edge)들로 구성되어 있습니다.
위상수학 또는 조합론에서는 그래프가 가진 연결성을 인접행렬과 같은 수치적인 도구로 표현하고 회로나 경로와 같은 특별한 연결성이 있는지 찾는 문제를 다루어 왔습니다.

그래프는 수학적으로 다음과 같이 정의됩니다.

> <span style="color:indianred">***Definition 1.1) Graph***</span>
> 
> **그래프**(Graph)는 점들의 집합 $V$와 점들의 순서쌍들의 집합 $E (\subseteq V\times V)$의 쌍, $G=(V,E)$로 정의된다.
> $V$의 원소를 **꼭짓점**(vertex)라고 하며, $E$의 원소 $(u,v) \in E$를 두 꼭짓점 $u$와 $v$를 연결하는 **변**(edge)이라고 한다.


<figure align = "center">
    <a href = "https://namu.wiki/w/%EC%BE%A8%EB%8B%88%ED%9E%88%EC%8A%A4%EB%B2%A0%EB%A5%B4%ED%81%AC%20%EB%8B%A4%EB%A6%AC%20%EA%B1%B4%EB%84%88%EA%B8%B0%20%EB%AC%B8%EC%A0%9C">
    <img src = 'https://w.namu.la/s/cb24070de98b93840315b899de9a78ee751cd22740d62058c24d52d9ec5585fed77f2c885ebae62994831a336e7d43a7c7215a7d7a9d4e62a71ddd05eda86280edf6c75010d134a5bb4dd2028423983e20d5c341bfc04f7062f8b4bf1366722ab2c7f416e0ed26ac48db6e28ca568d85'/>
    </a>
    <figcaption><b>사실 위상수학은 레온하르트 오일러가 쾨니히스베르크 다리 건너기 문제를 풀기 위해 그래프 개념을 도입하면서 탄생했다. [이미지 출처 : 나무위키 (이미지 클릭시 이동)]</b></figcaption>
</figure>





그래프는 거리나 위치의 개념과 상관없이 *두 대상이 연결되어 있는지 혹은 그렇지 않은지*만을 단순하게 표현하기에 좋기 때문에 네트워크 이론 등에서 많이 응용됩니다.
그래프는 두 점 사이의 일차원적인 연결성만 표현한다고 할 수 있습니다.
그래서 더 높은 수준의 연결성을 표현하고 싶다면 조금 더 고차원의 연결성으로 개념을 확장할 필요가 있습니다.

### §. 1.2.) Simplicial Complex

**심플리셜 컴플렉스**(Simplicial complex)는 꼭짓점과 변 뿐만 아니라 변들의 연결로 만들어진 삼각형, 삼각형의 연결로 만들어진 정사면체의 연결성 구조를 나타낸 대상으로, 그래프의 고차원 일반화라고 볼 수 있습니다.
심플리셜 컴플렉스의 수학적 정의는 다음과 같습니다.

>  <span style="color:indianred">***Definition 1.2) Simplicial Complex***</span>
> 
> 주어진 집합 $K$에 대하여, 다음 두 조건을 만족시키는 $K$의 부분집합들의 모임 $\mathcal{S}$를 생각하자.
>1. $\forall v\in K, \left\{v\right\}\in\mathcal{S}$
>2. $\tau \subseteq \sigma \in \mathcal{S} \implies \tau \in \mathcal{S}$
>
>이때, $(K,\mathcal{S})$를 **심플리셜 컴플렉스**(Simplicial complex)라고 한다. 
>문맥상의 의미가 명확하다면 $\mathcal{S}$를 생략하고 단순히 $K$로 표기하기도 한다.
>$\mathcal{S}$의 각 원소는 **심플렉스**(simplex)라고 부른다.
> 

이 정의를 찬찬히 살펴봅시다.
먼저 1번 조건이 의미하는 바는 주어진 집합 $K$의 각 원소는 심플리셜 컴플렉스의 기본단위가 되는 점들의 집합이 심플렉스가 된다는 말입니다.
그래서 그래프에서와 유사하게 심플랙스 $\left\{v\right\}\in \mathcal{S}$를 $K$의 **꼭짓점**(vertex)라고 부릅니다.

2번 조건의 의미는, 심플렉스 $\sigma$를 구성하는 파츠 $\tau$가 있다면, $\tau$도 심플리셜 컴플렉스를 구성하는 심플렉스라는 의미입니다.
그래프에 빗대어서 이 개념을 설명하자면, 그래프가 변 $(u,v)$을 포함한다면,  그것을 구성하는 꼭짓점들 $u,v$도 심플리셜 컴플렉스를 구성하는 심플렉스가 되어야 한다는 것입니다.

>  <span style="color:#2ECC71">***Example 1.1) Simplicial Complex***</span>
> 
>세 개의 꼭짓점들의 집합 $K=\left\{a,b,c\right\}$이 있다고 합시다.
>이때 세 꼭짓점과 그들을 각각을 연결하는 세 개의 변들, 그리고 그 세 변들로 둘러쌓인 삼각형의 모임을 $\mathcal{S}$로 두면 $(K,\mathcal{S})$는 삼각형의 연결성을 표현하는 심플리셜 컴플렉스가 됩니다.
>이때 삼각형 심플렉스 $\sigma$가 심플리셜 컴플렉스에 포함되므로 $\tau$를 구성하는 변 $\tau$도 심플리셜 컴플렉스의 구성에 포함이 되어야 합니다.
><figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial01.png?raw=true' width = 200></figure>
>
> 위 그림에서 심플리셜 컴플렉스 $(K,\mathcal{S})$의 심플렉스들의 모임 $\mathcal{S}$는 
>
>$$
>\mathcal{S} = \left\{\left\{a\right\},\left\{b\right\},\left\{c\right\},\left\{a,b\right\},\left\{b,c\right\},\left\{c,a\right\},\left\{a,b,c\right\}\right\}
>$$
>로 정의됩니다.


점을 0차원 선을 1차원으로 둔다면, 면은 2차원 공간을 3차원으로 두는 것은 우리가 일반적으로 *차원*이라는 단어를 생각할 때 떠올리는 관습입니다.
심플렉스들의 차원은 이와 유사한 대응으로 정의됩니다. 

심플렉스 $\sigma \in \mathcal{S}$가 **$k$-심플렉스**($k$-simplex)라고 하는 것은 $|\sigma| = k+1$인 경우를 말합니다.
즉, **(하나의 심플렉스를 구성하는데 필요한 꼭짓점들의 수 - 1)** 가 심플렉스의 차원이 됩니다.

0차원인 점을 구성하는 데엔 하나의 점이, 1차원인 선분을 구성하는 데엔 2개의 점이, 2차원인 삼각형을 구성하는 데엔 3개의 점이 필요하다는 점에서 이는 우리의 직관과 상응한다고 볼 수 있습니다.
다시 말해 꼭짓점은 0-심플렉스이고, 변은 1-심플렉스, 면은 2-심플렉스가 됩니다.

<figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial04.png?raw=true' width = 500></figure>


만약 두 심플렉스가 $\tau \subseteq \sigma$의 관계를 가지게 된다면, 더 작은 simplex $\tau$를 더 큰 simplex $\sigma$의 **면**(face)이라고 부르고, 더 큰 simplex $\sigma$를 더 작은 simplex $\tau$의 **여면**(coface)라고 부릅니다.


>  <span style="color:#2ECC71">***Example 1.2) 정사면체***</span>
> 
>심플렉스리셜 컴플렉스가 아래의 그림과 같은 정사면체와 그것을 구성하는 네 개의 삼각형, 여섯 개의 변,네 개의 꼭짓점으로 구성된다고 합시다.
>그러면 심플리셜 컴플렉스의 정의에 의해 정사면체 $\sigma$를 구성하는 각 삼각형들도 심플렉스이며, 이 삼각형 각각을 심플렉스 $\sigma$의 면이라고 합니다.
>이것은 우리의 기존 관습과 일치합니다.
>유의할 점은, 정사면체를 구성하는 각 변들과 각 꼭짓점들도 정의에 의해 정사면체의 면이라고 불린다는 점입니다.
> 또한 $\sigma$를 구성하는 각 변들과 꼭짓점들에게 있어서 $\sigma$는 각각에게 여면이 됩니다.
><figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial02.png?raw=true' width = 200></figure>




심플리셜 컴플렉스를 설명하면서 그림을 이용해 예시를 들었습니다.
사실 이 그림은 그냥 그려진 것이 아니고, 다음의 규칙에 따라 시각화한 것입니다.

><span style="color:#A569BD">***Remark) 심플리셜 컴플렉스의 시각화(Visualization)***</span>
> 
>$k$-심플렉스는 유클리드 공간 $\mathbb{R}^d\; (d \geq k)$ 상에 한 선분 위에 세 개 이상의 직선이 놓이지 않고 적절히 잘 흩어져 있는 $k+1$개의 점들로 만들어진 **볼록 도형**(convex hull)으로 시각화할 수 있다.
>이때 이렇게 흩어진 점들을 **어파인 독립**(affinely independent)하다고 한다.
>심플리셜 컴플렉스를 시각화할 구성하는 심플렉스들은 공통 면들끼리 접하도록 그려야 한다.

지금까지의 논의에서 심플렉스는 단순히 집합론의 언어만 사용했을 뿐, 일반적으로 기하학에 사용되는 좌표나 거리, 길이와 같은 개념을 전혀 사용하지 않았다는 점을 유의하세요.
위상수학은 최대한 이런 개념으로부터 자유로운 기하학을 다루기 때문에 무엇을 계산해야할지도 눈에 보이지 않고, 심지어 대상이 어떻게 시각화해야 하는지도 보이지 않을 수 있습니다.

보통의 데이터 사이언스나 머신러닝에서는 데이터를 무작정 유클리드 공간에 올려놓곤 합니다.
그러나 유클리드 공간에 정의된 좌표계나 거리의 개념은 데이터를 설명하는 데에 적절하지 않을 수 있습니다.

그러므로 TDA는 데이터를 심플리셜 컴플렉스로 표현하는 것으로 데이터가 가진 기하학적 특성을 추출합니다.
이렇게 추출된 특성은 좌표계의 선택이나 거리함수의 선택에 의존하지 않으므로 데이터에 대한 과도한 가정으로부터 오는 오류를 줄일 수 있습니다.

<figure align = "center">
    <a href = "https://en.wikipedia.org/wiki/Triangulation_%28topology%29">
    <img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Torus-triang.png/330px-Torus-triang.png'/>
    </a>
    <figcaption><b>심플리셜 컴플렉스로 표현된 토러스 [이미지 출처 : 위키피디아 (이미지 클릭시 이동)]</b></figcaption>
</figure>


### §. 1.3.) Filtration

만약 거대한 데이터 집합을 심플리셜 컴플렉스로 구현한다면 그것을 굉장히 복잡한 형태일 것입니다.
굉장히 복잡한 심플리셜 컴플렉스가 있다면, 그것을 한번에 관찰하기는 쉽지 않을 것입니다.
수학에서는 이런 복잡한 구조를 관찰하고자 할 때, 구조를 보존하는 작은 부분집합들을 분석해나가는 방법을 이용하곤 합니다.

지금 소개할 심플리셜 컴플렉스의 **필트레이션**(filtration)은 심플리셜 컴플렉스의 부분집합들을 점점 커지도록 나열하여서 현재의 심플리셜 컴플렉스가 어떤 과정을 통해 만들어졌을 지를 표현합니다.
TDA에서는 이러한 심플리셜 컴플렉스의 진화과정 속에서 연결성분이나 구멍과 같은 기하학적 정보가 얼마나 **지속**(persistent)되는지를 측정하고 이를 데이터의 중요한 특징으로 활용합니다.

<figure align = "center">
    <a href = "https://en.wikipedia.org/wiki/Triangulation_%28topology%29">
    <img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial05.png?raw=true'/>
    </a>
    <figcaption><b>TDA는 필트레이션을 이용해 데이터로부터 심플리셜 컴플렉스의 진화과정을 만들고, 그 과정 중에 연결성분(파란 막대)이나 구멍(점선)의 지속성을 측정한다.
    [이미지 출처 : Figure 1 in Otter, Nina, et al. "A roadmap for the computation of persistent homology." EPJ Data Science 6 (2017)]</b></figcaption>
</figure>


먼저 서브컴플렉스부터 정의해봅시다.
심플리셜 컴플렉스 $K$의 **서브컴플렉스**(subcomplex)는 심플리셜 컴플렉스가 되는 $K$의 부분집합 $L(\subseteq K)$를 말합니다.

>  <span style="color:#2ECC71">***Example 1.3) Sub Complex***</span>
> 
>Example 1.1에서 아래의 삼각형으로 시각화되는 심플리셜 컴플렉스 $(K,\mathcal{S})$를 정의했었습니다.
><figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial01.png?raw=true' width = 200></figure>
>
> 이때 $K$의 부분집합 $L = \left\{a,c\right\}$를 생각하고, $L$에 대한 심플렉스들의 모임 $\mathcal{T}$를 
>$$
>\mathcal{T} = \left\{\left\{a\right\},\left\{c\right\},\left\{a,c\right\}\right\}
>$$
>로 두면, $L$은 심플리셜 컴플렉스가 됩니다.
>따라서 $L$은 $K$의 서브컴플렉스가 됩니다.
>$L$은 위 그림에서 변 $\tau$로 시각화됩니다.


서브컴플렉스를 이용하면 주어진 컴플렉스의 작은 일부를 표현할 수 있습니다.
서브컴플렉스의 서브컴플렉스는 여전히 주어진 컴플렉스의 서브컴플렉스가 됩니다. (당연한 이야기 같지만, 훈련된 수학도라면 이는 당연한 일이 아닐 수 있음을 알아차려야 합니다.)
이런 과정을 반복하다보면, 언젠가는 공집합을 선택할 수 밖에 없게 될 것입니다.
이 과정을 통해 얻어진 서브컴플렉스들은 한 방향으로의 포함관계를 가지게 될 것입니다.
이러한 서브컴플렉스들의 배열을 **필트레이션**(filtration)이라고 부릅니다.


>  <span style="color:indianred">***Definition 1.3) Filtration***</span>
> 
> 심플리셜 컴플렉스 $K$의 서브컴플렉스들의 증가배열(nested subsequence)
> $$
\empty = K^0 \subseteq K^1 \subseteq \cdots \subseteq K^m = K$$
> 을 **필트레이션**(filtration)이라고 부른다.
> 이때 이러한 배열이 주어진 심플리셜 컴플렉스 $K$를 **필터드 컴플렉스**(filtered complex)라고 부른다. 
> 인덱스의 일반성을 위해 $K^i = K^m \; (i\geq m)$, $K^i = K^0 \; (i \leq 0)$ 으로 둔다.
>




>  <span style="color:#2ECC71">***Example 1.4) Filtration***</span>
> 
> 심플리셜 컴플렉스 $K$가 Example 1.2에서 주어진 정사면체로 표현된다고 합시다.
> 이때 $K$의 서브컴플렉스 $K$를 아래의 그림과 같이 정의합니다.
> 즉, $K^1$은 $K$의 한 꼭짓점, $K^2$는 그 꼭짓점을 포함하는 변, $K^3$은 그 변을 포함하는 면, $K^4$는 $K$ 자신으로 정의합니다.
> 그러면 배열 $\empty = K^0 \subseteq K^1 \subseteq K^2 \subseteq K^3 \subseteq K^4 = K$는 $K$의 필트레이션이 됩니다.
><figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial03.png?raw=true' width = 400></figure>


여기서는 자세히 설명하지는 않겠지만, 데이터로부터 필트레이션을 만드는 대표적인 방법을 하나 소개하도록 하겠습니다.
데이터가 **포인트클라우드** 타입으로 주어져 있다고 합시다.
그러면 다음과 같은 알고리즘으로 심플리셜 컴플렉스를 구축할 수 있습니다.

><span style="color:#A569BD">***Remark) 심플리셜 컴플렉스의 구축***</span>
>
> 포인트 클라우드 데이터 집합 $K$가 주어졌다고 하자.
> 거리 파라미터 $\epsilon \in [0,\infty)$에 대하여 다음 알고리즘을 생각하자.
> 1. 파라미터 $\epsilon$을 선택한다.
> 2. 두 점 사이의 거리가 $2\epsilon$ 이하가 되면 두 점을 변으로 연결한다. (즉, 각 점을 중심으로 반지름이 $\epsilon$인 원을 그려 두 원이 만나면 변으로 연결한다.)
> 3. 세 점에 대하여, 각각 두 점 사이의 거리가 $2\epsilon$ 이하가 되면 세 변을 삼각형으로 연결한다. (즉, 세 점이 변으로 서로 연결되어 삼각형을 그리면 그 삼각형을 면으로 채운다.)
> 
> 그러면 각 $\epsilon$에 대하여, $K$를 꼭짓점으로 하는 심플리셜 컴플렉스 $K_\epsilon$이 만들어진다.
> 이러한 심플리셜 컴플렉스를 **비에토리스-립스 컴플렉스**(Vietoris-Rips Complex) 또는 **립스 컴플렉스**라고 부른다.
> 
> 이때 충분히 큰 두 파라미터 $\epsilon < \epsilon'$에 대해 $K_{\epsilon} = K_{\epsilon'}$이므로, 가장 큰 심플리셜 컴플렉스 $K$를 선택할 수 있다.
> 이제 $\epsilon$들의 수열 $0 = \epsilon_0 \leq \epsilon_1 \leq \epsilon_2 \leq \cdots \leq \epsilon_n$을 택하면, 필트레이션 
>$$
\empty = K_0 \subseteq K_{\epsilon_1} \subseteq K_{\epsilon_2} \subseteq \cdots \subseteq K_{\epsilon_n} = K$$
>를 얻는다. 
> 이를 **비에토리스-립스 필트레이션**(Vietoris-Rips filtration) 또는 **립스 필트레이션**이라고 부른다.
>
> <figure align = "center">
>    <a href = "https://www.geogebra.org/m/ye79r6ws">
>    <img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial.gif?raw=true'/>
>    </a>
>    <figcaption><b>립스 컴플렉스가 만들어지는 과정 [GIF 출처 : GeoGebra (Author : Vaibhav Karve)]</b></figcaption>
></figure>

TDA에서 가장 먼저 데이터를 처리하는 방법은 데이터 타입에 적절한 필트레이션을 구축하는 것입니다. 
적절한 필트레이션을 찾은 뒤에는 파라미터가 점점 증가시켜가면서 심플리셜 컴플렉스의 연결관계에가 어떻게 변해가는지 관측합니다.
이를 위해서 심플리셜 컴플렉스라는 기하학적 대상을 계산이 가능한 대수적 대상으로 대응시키는 과정이 필요합니다.
이때 등장하는 개념이 **호몰로지**(Homology)입니다.

다음 포스팅에서는 무시무시한 호몰로지에 대해서 다루어보겠습니다.

---

> 📝 **요약 Summary**
> - TDA는 데이터의 연결성을 표현하기 위해 심플리셜 컴플렉스라는 도구를 사용한다.
> - 복잡한 연결성을 분석하기 위해 작은 심플리셜 컴플렉스에서부터 점점 진화시켜나가는 필트레이션 기법을 사용한다.
> - TDA는 이 필트레이션 과정에서 심플리셜 컴플렉스가 가진 기하학적 특징의 변화를 감지해 데이터의 특징으로 삼는다.
> 


