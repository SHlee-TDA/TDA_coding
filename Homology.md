
## 2. Homology

> 📌 **핵심 Keyword**
> - **체인 모듈** : 심플렉스 간에 연산을 정의해 만든 벡터공간.
> - **바운더리 오퍼레이터** : $k$-심플렉스를 그것을 둘러싼 $(k-1)$-심플렉스들의 합으로 대응시키는 선형변환
> - **호몰로지** : 
> 




### §. 2.1.) Chain module

[지난 포스팅](https://velog.io/@shlee0125/TDA%EC%9D%98-%EA%B8%B0%EC%B4%88-01.-Simplicial-Complex)에서는 데이터를 기하학적으로 표현하기 위해 심플리셜 컴플렉스라는 개념을 사용한다고 배웠습니다. 
특히 심플리셜 컴플렉스를 통해 알고싶은 기하학적 정보는 **연결성**과 관련되어 있다고 했습니다.
이번 포스팅에서는 연결성에 의해 정의되는 기하학적 특징은 무엇인지, 그것을 어떻게 효과적으로 계산할 수 있는지 나타내는 도구를 배울 것입니다.

심플리셜 컴플렉스 $K$가 주어졌다고 합시다.
자연수 $k$에 대하여, $\Sigma_k$를 $K$에 존재하는 $k$-심플렉스들의 집합이라고 합시다.
예를들어, $\Sigma_0$는 꼭짓점들만 들어있는 집합, $\Sigma_1$는 변들만 들어있는 집합일 것입니다.

이 집합들은 그저 집합일 뿐, 아무런 구조가 없습니다.
수학자들은 이런 집합 위에 적절한 구조를 생각하여 유용한 정보를 얻는 방법을 많이 사용합니다.
특히 이런 집합 위에 벡터공간 구조를 적절히 줘서 선형대수학이 잘 작동하도록 하는 방법은 굉장히 유용하며 강력한 도구입니다.
그러나 이 이론을 설명하고자 하면 수학과 대학원 1학년 수준의 대수학을 들고와야 하므로 여기선 직관적으로 설명만 하도록 하겠습니다.

$k$-컴플렉스들의 집합 $\Sigma_k$에 덧셈을 **두 $k$-컴플렉스를 병렬배치(Juxtaposition)하는 것**이라고 나이브하게 정의해보겠습니다.
이 연산이 직관적으로 작동하는 방법은 아래 **Example 2.1**에 설명되어 있습니다.
심플리셜 컴플렉스들의 연산을 위와 같이 정의하면, 연산이 닫혀있게 하기 위해서 집합은 더욱 커져야 합니다. 
즉 $\Sigma_k$의 원소들을 기본 단위(basis)로 해서 이들의 합으로 만들 수 있는 모든 조합을 포함하는 집합이어야 합니다.
정확히 말하자면, 계수가 $0$ 또는 $1$인 선형결합 
$$
a_0x_1 + a_1x_1 + \cdots + a_nx_n \; (a_i \in \left\{0,1\right\}, x_i \in \Sigma_k)
$$
을 모두 포함하는 집합이어야 합니다.
이때, 계수가 2가 되면 0이 되도록 합니다. 
이렇게 만들어진 새로운 집합은 수학적으로 계수(스칼라)가 유한체 $\mathbb{F}_2 = \left\{0,1\right\}$인 벡터공간이 됩니다.
이러한 공간을 **체인 모듈**(Chain module)이라고 합니다.





> <span style="color:indianred">***Definition 2.1) Chain Module***</span>
> 
> 주어진 심플리셜 컴플렉스 $K$에 대하여, $k$-심플렉스들의 집합을 $\Sigma_k$라고 하자. 
> $\Sigma_k$를 기저(basis)로 하고, $\mathbb{F}_2 = \left\{0,1\right\}$를 계수로 하는 벡터 공간
> $$
>C_k(K) = \left\{a_1x_1 + \cdots +a_nx_n : a_i \in\mathbb{F}_2, x_i \in \Sigma_k  \text{ for all } i \right\}
> $$
> 을 $K$의 **$k$-체인 모듈**(*k*th Chain module)라고 한다.
> 
> $C_k(K)$ (또는 $C_k$로 표기)의 원소 $\sigma = a_1x_1 + \cdots + a_nx_n$을 **$k$-체인**($k$-chain)이라고 부른다.
>

><span style="color:#A569BD">***Remark) Free module theory (읽지 마세요.)***</span>
>
><figure align = "center">
>    <img src = 'https://image.fmkorea.com/files/attach/new/20210115/486616/171939074/3328814988/f91cfe0b4f4c99a5c8623e978c980413.jpeg'/ >
>    </a>
>    <figcaption><b>뒤로가기 누를까?</b></figcaption>
></figure>
>
> 수학적으로 위와 같이 집합 $X$으로부터 만들어진 벡터공간을 $X$로부터 생성된 프리 $\mathbb{F}_2$-모듈(Free $R$-module)이라고 부릅니다.
> 더욱 일반적으로, 임의의 환(ring) $R$과 집합 $X$에 대하여, $X$의 원소만큼의 직접합(direct sum) $\oplus_{X} R$과 $R$-가군 동형($R$-module isomorphic)인 $R$-가군 $F$가 존재하며, 이러한 $R$-모듈 $F$를 **$X$에 의해 생성된 프리 $R$-모듈**(Free $R$-module)이라고 부릅니다.
>
> TDA를 일반화된 이론으로 다루는 문헌들에서는 체인 벡터스페이스 대신 계수 환을 $\mathbb{Z}$로 택하여, 가환군을 생각해 체인 그룹으로 두기도 합니다. [Carlsson, 2005]
> 
> 유한집합에 의해 생성된 프리 모듈은 굉장히 강력한 이론들을 가지고 있습니다.
> 조금 과장을 보태서 선형대수학에서 배운 기저를 이용해서 만든 강력한 계산 도구들(행렬 이론)과 이론(선형변환 이론)들을 전부 사용할 수 있습니다.
> 이 이론에 대해 이야기하고 싶은 것은 너무 많지만, 참고도서만 남겨둔 채 먼 미래로 기약하기로 하겠습니다.
> 
> **[Reference]**
>
> 1. Introduction to Commutative Algebra (Michael Atiyah and lan G. Macdonald).
> 2. Abstract Algebra (Dummit and Foote)
> 3. Algebra (Thomas W. Hungerford)
> 



>  <span style="color:#2ECC71">***Example 2.1) Chain Module***</span>
> 
>아래의 그림과 같이 시각화되는 심플리셜 컴플렉스 $K$가 있다고 합시다.
>그러면 이 경우 $\Sigma_0 = \left\{\left\{a\right\}, \left\{b\right\} ,\left\{c\right\}\right\}$, $\Sigma_1 = \left\{\left\{a,b\right\}, \left\{b,c\right\} ,\left\{c,a\right\}\right\}$, $\Sigma_2 = \left\{\left\{a,b,c\right\}\right\}$ 입니다.
><figure align = 'center'><img src = 'https://github.com/SHlee-TDA/TDA_coding/blob/master/images/simplicial01.png?raw=true' width = 200></figure>
>
> 이제 $k$-컴플렉스들의 집합 $\Sigma_k$에 덧셈을 **두 $k$-컴플렉스를 병렬배치(Juxtaposition)하는 것**이라고 나이브하게 정의해보겠습니다.
> 예를들어, 두 꼭짓점 $\left\{a\right\} ,\left\{b\right\}\in \Sigma_0$의 덧셈 $\left\{a\right\}+\left\{b\right\}$의 결과는 아래의 그림과 같이 두 개의 점이 병렬배치된 그림으로 시각화할 수 있습니다.
><figure align = 'center'><img src = 'images\chain_complex01.png' width = 200></figure>
>
> 유사하게, 두 변 $\left\{a,b\right\} ,\left\{b,c\right\}\in \Sigma_1$의 덧셈 $\left\{a,b\right\} + \left\{b,c\right\}$는 아래의 그림과 같이 두 개의 변이 병렬배치되어 연결된 그림으로 시각화할 수 있습니다.
> <figure align = 'center'><img src = 'images\chain_complex02.png' width = 200></figure>
> 
> 특별히 같은 $k$-심플렉스끼리의 합은 0이 됩니다. 
> 이 경우에는 같은 심플렉스가 겹치면서 사라진다고 생각하면 좋습니다.
> 

체인 모듈을 정의하는 것에 고급 수학이론이 다소 첨가되어 어려움이 있었을 것입니다.
이 정의를 어떻게 구성하는 데에 완벽히 이해할 필요는 없습니다.
그 이론적 구성을 잘 쌓아둔 수학자들을 믿고 감사하며, 예제로서 현상만 이해하는 것을 권해드립니다.

체인 모듈을 정의한 이유는 단순히 기하학적 대상이었던 심플리셜 컴플렉스에 **선형대수학**을 응용하기 위함입니다.
이제부터는 정말 선형대수학 이야기만 있을 것입니다.
선형대수학에 익숙하신 여러분은 마치 **한 조각 케이크🍰 먹듯** 손쉽게 이 포스팅의 마지막까지 읽으실 수 있을 것입니다.




<figure align = "center">
    <img src = 'https://image.fmkorea.com/files/attach/new/20210115/486616/171939074/3328814988/78bf18a5e229c025e987e0ed342ade01.jpeg' width = 200/>
    </a>
    <figcaption><b>따악 한 섹션만 더 읽어주십시요. 반드시 이해하실 수 있도록 쉽게 설명해드리겠습니다!!</b></figcaption>
</figure>





### §. 2.2.) Boundary operator

벡터공간 이야기가 나온 김에 선형대수학의 주요 개념들과 정리 몇 가지를 나열해보겠습니다.

><span style="color:#A569BD">***Remark) 선형대수학 사전***</span>
> - **Vector Space** : 선형대수학에서 다루는 대수적 구조. 덧셈과 스칼라곱 두 가지 연산이 잘 정의된 공간이다. 
> - **Basis** : 벡터공간의 모든 원소를 표현할 수 있는 대표들. 벡터 공간의 모든 원소들은 기저들의 선형결합에 의해 표현된다.
> - **Dimension** : 한 벡터공간의 특징을 표현할 수 있는 수. 기저의 원소 개수를 그 벡터공간의 차원이라고 한다. 
> - **Linear map (Linear Transformation)** : 두 벡터공간 사이의 함수로서, 덧셈과 스칼라곱 연산을 보존한다. 
> - **Linear Extension Theorem** : 선형변환은 정의역의 모든 원소를 대응시켜줄 필요없이, 기저들의 대응만 맞춰줘도 전체를 알 수 있다.
> - **Rank-Nullity Theorem** : 유한차원 벡터공간 $V$와 


 
이제 심플리셜 컴플렉스를 꼭짓점, 변, 면으로 따로 떼어서 벡터공간 $C_0(K), C_1(K), C_2(K), \ldots$을 만들었습니다.
이들을 잘 분석하면 심플리셜 컴플렉스에 대한 유용한 정보를 많이 알 수 있을 것입니다.

선형대수학에서 벡터공간을 만나면 가장 먼저 **기저와 차원**을 확인했었습니다.
$k$-체인 모듈 $C_k$의 **기저**(basis)는 정의했던 대로 $\Sigma_k$의 원소들입니다. 
따라서 $k$-체인 모듈의 **차원**(dimension)은 $|\Sigma_k|$이며, 이는 심플리셜 컴플렉스 $K$의 $k$-심플렉스들의 수와 같습니다.

표기법 하나를 정하고 가겠습니다.
>  <span style="color:#F39C12">***Notation)***</span>
> 
> $k$-심플렉스 $\sigma \in \Sigma_k$가 $k+1$개의 꼭짓점 $v_0, v_1,\ldots, v_k \in \Sigma_0
$에 의해 결정된다고 하자.
> 즉, $\sigma = \cup_{i=0}^k v_i\in \mathcal{S}$이다. 
> 이 경우 $\sigma = [v_0,v_1,\ldots,v_k]$로 표기한다.
> 이때 $\sigma$에 대응하는 $k$-체인은 표기를 남용하여, 그대로 $\sigma (\in C_k)$로 표기한다.
>
> $\sigma = [v_0,v_1\ldots, v_k]$에서 꼭짓점 $v_i$를 제거해 만들어진 $(k-1)$-심플렉스는 $[v_0,v_1\ldots, \hat{v_i},\ldots,v_k] \in C_{k-1}$로 표기한다.


이번에는 서로 다른 체인 모듈간의 관계를 알기 위해 선형변환을 만들어볼 것입니다.
선형대수학의 가장 중요한 정리 중 하나는 선형변환을 결정할 때 일반 함수처럼 정의역에 있는 모든 원소에 대한 대응을 결정해줄 필요없이, 정의역의 기저가 어디로 대응될지만 결정해주면 된다는 **Linear Extension Theorem** 입니다.

>  <span style="color:#3498DB">***Theorem 2.1) Linear Extension Theorem***</span>
> 
> $\left\{v_1, \ldots, v_n\right\}$, $\left\{w_1, \ldots, w_n\right\}$을 각각 벡터공간 $V$와 $W$의 기저라고 하자.
> 그러면 각 $i=1,2,\ldots,n$에 대하여, 
>
> $$
>Tv_i = w_i
>$$
> 가 되게 하는 선형변환 $T : V\rightarrow W$가 유일하게 존재한다.
> 
> [참고 : Theorem 3.5 in Linear algebra done right (Sheldon Axler) 그외 임의의 선형대수학 교과서]

위 정리에 따르면, 우리는 체인 모듈의 기저가 되는 $k$-심플렉스를 어디로 대응시켜줄지 결정하기만 하면 선형변환을 정의할 수 있습니다.
이제 체인모듈들을 어떤 관계로 관찰할지 상상력만 발휘하면 이론과 계산 도구는 이미 다 준비된 셈입니다.

똑똑한 수학자들은 높은 차원의 심플렉스는 낮은 차원의 심플렉스들로 둘러쌓여 있다는 점에 주목했습니다. 
예를들어서, 2차원 심플렉스 삼각형면은 1차원 심플렉스인 세 변으로 둘러쌓여 있습니다.
이들 세 변은 삼각형의 **테두리**(Boundary)라고 할 수 있습니다.
그래서 높은 차원의 심플렉스를 그것을 둘러싼 경계로 대응시키는 관계를 생각하기로 했습니다.
이를 **바운더리 오퍼레이터**(Boundary operator)라고 부릅니다.

바운더리 오퍼레이터의 정의는 다음과 같습니다.

>  <span style="color:indianred">***Definition 2.2) Boundary Operator***</span>
> 
> 심플리셜 컴플렉스 $K$의 연속한 체인모듈 $C_k, C_{k-1}$들에 대하여, 선형변환 $\partial_k : C_k \rightarrow C_{k-1}$를 다음과 같이 정의하자.
> $$
>\partial_k \sigma = \sum_{i=0}^k [v_0,\ldots, \hat{v_i} \ldots, v_k]\;\; \text{ for all } \sigma = [v_0,\ldots,v_k] \in \Sigma_k$$ 
>
>여기서 각 $\sigma = [v_0,\ldots, v_k]$는 $C_k$의 기저가 되므로, Theorem 2.1 (Linear Extension Theorem)에 의해 이러한 선형변환 $\partial_k$는 유일하게 존재한다.




>  <span style="color:#2ECC71">***Example 2.2) Boundary Operator***</span>
> 
>세 꼭짓점 $v_0, v_1, v_2$로 결정되는 2-심플렉스 $\sigma = [v_0,v_1,v_2] \in C_2(K)$가 있다고 합시다. 
>$\sigma$는 세 변 $[v_0,v_1], [v_1,v_2],[v_2,v_0]$로 둘러쌓여 있습니다.
>따라서 바운더리 오퍼레이터 $\partial_2$에 대한 $\sigma$의 이미지는 $[v_0,v_1] + [v_1,v_2] + [v_1,v_2] \in C_1$입니다.
> 아래의 그림을 보시면 시각적으로 바운더리 오퍼레이터가 어떤 작용을 하는지 관찰할 수 있습니다.
><figure align = 'center'><img src = 'images/chain_complex03.png'></figure>
> 


위 예제에서 살펴볼 수 있듯, 바운더리 오퍼레이터는 심플렉스를 입력하면 그 테두리를 뱉어주는 함수입니다.
이러한 바운더리 오퍼레이터들에 의해서 체인 모듈들은 하나의 수열처럼 연결시킬 수 있습니다.
이러한 나열을 **체인 컴플렉스**(Chain Complex)라고 합니다.

지금까지의 내용을 정리해봅시다.
1. 데이터의 기하학적 특징을 관찰하기 위해 심플리셜 컴플렉스 형태로 표현했습니다.
2. 심플리셜 컴플렉스를 분석하기 위해 각 차원별 컴플렉스로 분리해 체인모듈이라는 벡터공간을 생각했습니다.
3. 체인모듈들을 바운더리 오퍼레이터로 연결시켰습니다.

이제 남은 일은 이 관계로부터 구체적으로 기하학적 특징을 계산해내기만 하면 됩니다.
그것이 다음 섹션에서 다룰 **호몰로지**(Homology)입니다.

이름부터 무서운 호몰로지에 대해 이야기하기에 앞서, 지금까지 논의에서 선형대수학을 적극적으로 사용하였는데 이렇게 하였을 때 얻는 장점에 대해 잠시만 생각해보겠습니다.

우리는 선형대수학을 이용해 우리의 직관 속에 있던 **심플렉스를 넣으면 그 테두리를 뱉어주는 함수**를 쉽게 정의할 수 있었습니다.
선형대수학이 가진 또 하나의 강력한 힘은 **선형변환을 행렬로 표현할 수 있다**는 점입니다.
선형변환은 순전히 인간의 언어로 표현된 규칙입니다.
그러므로 이를 컴퓨터에게 가르쳐주기란 쉽지 않을 것입니다.
그러나 이를 행렬로 표현해 숫자들의 나열로 컴퓨터에게 입력해준다면, 컴퓨터는 이를 쉽게 이해하며 사람이 하기 어려운 복잡한 계산도 줄곧 해냅니다.

이 점을 응용하면 복잡하고 큰 데이터에 대한 기하학적인 성질을 분석하는 일도 컴퓨터에게 맡길 수 있게 됩니다.
이것이 TDA가 데이터 분석에 응용될 수 있는 실용적인 이유입니다.



<figure align = "center">
   <img src = 'https://img.livescore.co.kr/data/editor/2103/8e703a59a514ebee2b50c77c80b2fed0.JPG'/ width = 200>
    </a>
    <figcaption><b>그래서 교수님들이 선형대수학을 그렇게 공부하라고 하셨었구나?!</b></figcaption>
</figure>



### §. 2.3.) Homology

선형변환을 정의하고 나면 숨쉬는 것처럼 해야할 일은 **커널**(Kernel)과 **이미지**(Image)를 구하는 것입니다.
행렬의 언어로 이야기하자면, **영공간**(Null space)와 **열공간**(Column space)를 구하는 것입니다.

바운더리 오퍼레이터의 커널과 이미지는 기하학적인 특징 때문에 특별히 각각 **사이클 그룹**과 **바운더리 그룹**이라고 부릅니다.

>  <span style="color:indianred">***Definition 2.4) Cycle group and Boundary group***</span>
> 
> 심플리셜 컴플렉스 $K$의 연속한 체인모듈 $C_k, C_{k-1}$들에 대하여, 선형변환 $\partial_k : C_k \rightarrow C_{k-1}$를 다음과 같이 정의하자.
> $$
>\partial_k \sigma = \sum_{i=0}^k [v_0,\ldots, \hat{v_i} \ldots, v_k]\;\; \text{ for all } \sigma = [v_0,\ldots,v_k] \in \Sigma_k$$ 
>
>여기서 각 $\sigma = [v_0,\ldots, v_k]$는 $C_k$의 기저가 되므로, Theorem 2.1 (Linear Extension Theorem)에 의해 이러한 선형변환 $\partial_k$는 유일하게 존재한다.




---


> 📝 **요약 Summary**
> - TDA는 데이터의 연결성을 표현하기 위해 심플리셜 컴플렉스라는 도구를 사용한다.
> - 복잡한 연결성을 분석하기 위해 작은 심플리셜 컴플렉스에서부터 점점 진화시켜나가는 필트레이션 기법을 사용한다.
> - TDA는 이 필트레이션 과정에서 심플리셜 컴플렉스가 가진 기하학적 특징의 변화를 감지해 데이터의 특징으로 삼는다.
> 