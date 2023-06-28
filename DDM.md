

## 引言

决策与我们的日常生活息息相关，无论是过马路、购物，还是商业投资与政治决策，都需要我们做出不同的决策。决策最通俗的定义是个体在刺激的影响下发成的心理与行为变化，根据其涉及的不同范畴，将其分为以下三类：

决策表现出的形式：稳定与非稳定的决策，例如，每次都选择左边食堂就是稳定的决策，而在形成稳定决策之前去各个食堂进行尝试的过程就是非稳定的决策。快速与慢速的决策，例如，决定是向左还是向右超过前面的车一般是在认知水平较低的情况下快速做出的，而投票给哪位候选人或买哪辆车则需要经过长时间的深思熟虑—在双加工理论中T1过程表示更快跟自动化的加工，而T2过程表示更深思熟虑的分析(Evans, 2008)。二元与多元决策，即在两个选项中进行决策还是多个选项进行决策。此外决策的形式还有简单与复杂的决策、随机与偏向性的决策等。

外界刺激对决策的影响：不同的刺激类型对决策的影响也会不同，比如金钱决策与道德决策存在明显的认知与行为差异(Conitzer et al., 2017)。强化学习理论表明，决策后呈现的后果(奖励或是惩罚)会影响后续的决策(Miletić et al., 2021)。框架效应表明，对于同一问题不同的描述也会对决策产生影响。更重要的是最近的研究已经开始探讨社会环境对于决策的影响，比如内外群体认同对决策的影响、从众对决策的影响(Cruwys et al., 2021; Tump et al., 2020; Zhang & Gläscher, 2020)。

个体因素对决策的影响：个体的认知、情感、动机与人格特征都会影响决策行为。但决策的核心问题始终是人的决策行为是否理性？哪些因素导致了人们决策的不理性？近年对于该问题探讨最多源自价值偏向、思维倾向等主题(Fischhoff & Broomell, 2020)。

DDM(drift diffusion model)模型认为，人们的行为决策背后往往存在一个信息收集的过程，当收集到的信息超过某个阈值，决策就产生了。比如，在面临选择哪个食堂时，大脑会对两个食堂的各种信息进行比较(信息收集的过程)，如果做出左边食堂环境与味道更能使自己满足的判断(信息超过阈值)，那么决策行为就会产生(选择吃饭而不是选择不吃)。可见，DDM的本质在于将感知表征与记忆中存储的知识快速匹配，这使我们能够识别眼前环境中的事物，并决定我们应该如何应对它们。

因此，DDM描述的决策行为属于个体存在一定价值倾向时稳定而又快速的决策 ，而背后对应的正是基于价值的决策理论(value-based decision)(Ratcliff et al., 2016)。值得注意的是，最初的DDM模型只适用于二元决策任务，即只存在两个备选项时的决策任务，通过数十年的发展，该理论模型对于解释行为决策的优良性已经得到了很好的验证(Ratcliff, 1978)。

本文的目的在于用通俗易懂的方式介绍DDM(drift diffusion model)的数学模型，阐述DDM模型与价值决策之间的关系，并通过实例介绍如何进行数学建模。

漂移扩散模型(DDM)认为，决策是一个在噪音中收集信息的过程，当收集到的信息超过某个阈值，决策就产生了。那什么是漂移扩散？什么是噪音与信息？什么又是阈值呐？

## 漂移扩散过程drift & diffusion processing

### 什么是漂移drift？

漂移指具有方向偏向性的运动过程。比如，小明喜欢香蕉但不喜欢苹果，那么小明在选择这两种水果时只会选择香蕉而不会选择苹果，这就是具有方向性的决策。而漂移是通过其漂移过程来体现的，比如从不喜欢任何水果到只喜欢香蕉。可见，漂移过程必然具有起点(不喜欢水果)，结果(喜欢香蕉)，方向(是喜欢香蕉而不是其他水果)，三个特性。

### 什么是扩散diffusion？

相对于漂移的有方向性运动，扩散指随机的扩散运动过程。比如，小明有时喜欢吃香蕉而有时喜欢吃苹果。此时，小明对于选择何种水果是没有稳定的方向性的，这就是扩散过程。扩散表明了生活中的一种本质规律，好似情绪，我们渴望得到快乐但是情绪却一直在波动(diffusion processing)。

### 漂移扩散过程drift diffusion processing

想要达到漂移的结果(即喜欢香蕉)，有时并没有我们想的那么容易，即我们的生活中不止有香蕉一种水果，并且不可能通过几次的尝试就只选择香蕉而不考虑其他水果。最有可能的情况是，第一吃的香蕉还没熟导致小明不喜欢香蕉，但是后来逐渐发现一般情况下香蕉还是比苹果更好吃的。

因此，漂移扩散过程是对曲折人生过程的描述，而不仅是对某个决策结果的描述。既然该模型描述的对为一个曲折的过程，就必然存在起点、随着时间的变化与结果三个部分。如图1中的曲线，很好的描述了每个决策中漂移扩散的三个部分(Johnson et al., 2017)。

![](https://pic4.zhimg.com/v2-fee5767a33f3bb834fa8f3f90d2746b3_b.jpg)

图1 DDM中信息的累积过程

漂移扩散过程对于心理学的意义：通过数学形式来表现人们在决策时心理动态变化的过程，即如何在两个选项中"纠结"的做出选择。

## 如何通过数学符号来表现这个问题？

虽然我们知道DDM的数学意义，但是如何通过数学符号来描述漂移扩散dd过程(drift diffusion processing)呐？

$V\left(t\right)=V\left(t-1\right)+µ+εt$V\\left(t\\right)=V\\left(t-1\\right)+µ+εt \----公式1 注意：此时的t是步数step，而不是反应时rt

公式1的意义在于体现dd过程。其中V(t)指此刻个体赋予某一选项(比如选择吃香蕉)的主观价值，其值越高表明对其偏好越强，即越有可能选择它。V(t-1)表示上一时刻对于该选项的主观偏好，即有可能上一时刻喜欢香蕉也有可能上一时刻喜欢苹果，可见，上一时刻与此刻的主观偏好越是一致，那么偏好值上涨的速度越快，即越快选择某一选项。其中μ指漂移率，ε(t)指此刻的扩散的程度，与上文提到的漂移扩散过程中的概念一一对应。可见，μ指明了决策的方向(即选择香蕉还是苹果)，其值越大偏好值上涨的速度越快，而ε表明了决策中"纠结"的程度，其值与μ越一致对偏好变化的影响越小(即越不纠结)，相反，其值与μ越不一致对偏好变化的影响越大(即难以在两种水果间做出选择)。

公式1的意义在于体现dd过程。其中V(t)指此刻个体赋予某一选项(比如选择吃香蕉)的主观价值，其值越高表明对其偏好越强，即越有可能选择它。V(t-1)表示上一时刻对于该选项的主观偏好，即有可能上一时刻喜欢香蕉也有可能上一时刻喜欢苹果，可见，上一时刻与此刻的主观偏好越是一致，那么偏好值上涨的速度越快，即越快选择某一选项。其中μ指漂移率，ε(t)指此刻的扩散的程度，与上文提到的漂移扩散过程中的概念一一对应。可见，μ指明了决策的方向(即选择香蕉还是苹果)，其值越大偏好值上涨的速度越快，而ε表明了决策中"纠结"的程度，其值与μ越一致对偏好变化的影响越小(即越不纠结)，相反，其值与μ越不一致对偏好变化的影响越大(即难以在两种水果间做出选择)。

虽然我们通过数学符号描述了dd过程，但是如何计算漂移率与扩散度呐？

首先，假设小明选择香蕉的概率P=0.6，选择苹果的概率Q=0.4，可见小明对于选择香蕉是有偏好的(即存在方向性的漂移而不是随机选择P=0.5)。但在小明真正做出选择之前，小明会每隔一秒进行一次预决策，比如在t=0s时小明选择了香蕉，那么V(0)=1，如果t=1s时小明再次选择香蕉那么V(1)=V(0)+1=2，如果小明选择了苹果则V(1)=V(0)-1=0。在t=10s时，如果V(10)大于0那么小明选择香蕉，如果V(10)小于0，那么小明选择苹果。可见，选择香蕉的概率P影响了模型中的参数μ与ε。而每一次预选择则是DDM模型定义中的信息收集过程(evidence cumulative processing)。

那么，如何通过概率P计算μ与ε呐？

$V_n=V_{n-1}+B_x=V_{n-1}+\mu+\varepsilon\ \ \ \ \ 公式2$V\_n=V\_{n-1}+B\_x=V\_{n-1}+\\mu+\\varepsilon\\ \\ \\ \\ \\ 公式2

上述的例子可以用公式2表示，当选择x=香蕉时 B=1，当选择x=苹果时 B=0。可见B=μ+ε，即漂移扩散过程等价于伯努利随机抽样过程(类似于投正面出现概率P=0.6的硬币)。

$V_n=V_{n-1}+log\frac{p_A\left(x_n\right)}{p_B\left(x_n\right)} =V_{n-1}+\frac{\left(\mu_A-\mu_B\right)^2}{\sigma_B^2}+\frac{\mu_A-\mu_B}{\sigma_B^2}\epsilon,\mathrm{where\epsilon}\sim\mathcal{N}\left(0,1\right)\ \ 公式3$V\_n=V\_{n-1}+log\\frac{p\_A\\left(x\_n\\right)}{p\_B\\left(x\_n\\right)} =V\_{n-1}+\\frac{\\left(\\mu\_A-\\mu\_B\\right)^2}{\\sigma\_B^2}+\\frac{\\mu\_A-\\mu\_B}{\\sigma\_B^2}\\epsilon,\\mathrm{where\\epsilon}\\sim\\mathcal{N}\\left(0,1\\right)\\ \\ 公式3

根据公式3，先把P转化为似然比 $\frac{p_A\left(x_n\right)}{p_B\left(x_n\right)}$\\frac{p\_A\\left(x\_n\\right)}{p\_B\\left(x\_n\\right)} ，其中，PA代表苹果出现的概率，PB代表香蕉出现的概率，xn为反应时，表达了在某一次决策时当反应时为xn的情况下选择苹果的概率比选择香蕉的概率大多少。从公式可见，当PA>PB，似然比为正数，当PA<PB，似然比为负数。这样做的好处在于引入了反应时(因为实验数据常常会记录反应时，并且DDM模型源自于信号检测论)的同时，可以把似然比分成两个部分 $\frac{\left(\mu_A-\mu_B\right)^2}{\sigma_B^2}+\frac{\mu_A-\mu_B}{\sigma_B^2}\epsilon$\\frac{\\left(\\mu\_A-\\mu\_B\\right)^2}{\\sigma\_B^2}+\\frac{\\mu\_A-\\mu\_B}{\\sigma\_B^2}\\epsilon ，而这两个部分恰好就是μ与ε。

当我们从收回的数据中得到两个选项的反应时分布时，就可以计算μ与ε。如图2，通过可视化的方式表现evidence cumulative processing，即dd过程。其中不同颜色的曲线代表不同被试，虚线就是前文中提到用V(10)>0去判断选择行为的阈值。

![](https://pic3.zhimg.com/v2-691a84f8eec5f73e02989dc38168d53a_b.jpg)

图2 不同被试的信息累积过程

### stop with boundary or time

问题好似都被解决了，但回顾DDM的定义，即当信息累积超过阈值时决策产生，那么阈值是否被体现了呐？

在前面的例子中，并不是信息累积超过阈值时dd过程才结束从而产生行为决策，而是我们规定了当t=10s，去对比V(10)与0这个阈值的关系，这并不符合DDM的定义。因此，如何设置一个阈值(threshold)使得dd过程中的价值偏好V(t)一旦累积到这个界限(boundary)就自动停止并做出决策呐？

$\alpha=\frac{1}{1+\exp{\left(\left|V_t\right|\right)}}\ \ \ \ 公式4$\\alpha=\\frac{1}{1+\\exp{\\left(\\left|V\_t\\right|\\right)}}\\ \\ \\ \\ 公式4

根据公式4，我们可以人为的设置一个参数α作为阈值，通过这个阈值α倒推出Vt的值，使得实际的Vt大于此值时就停止信息的收集。根据图1，由于DDM模型中的决策有两个选项，因此存在两个阈值，即α代表选项A，-α代表选项B(当Vt小于-α意味选择选项B)。

当把α也加入公式3中，根据(Feller, 1968)的推导，得到如公式5。

$f\left(t\middle|v,a,z\right)=\frac{\pi}{a^2}\mathrm{exp}\left(-vaz-\frac{v^2t}{2}\right)\times\sum_{k=1}^{\infty}kexp\left(-\frac{k^2\pi^2t}{2a^2}\right)\mathrm{sin} \left(k\pi z\right)\ \ 公式5$f\\left(t\\middle|v,a,z\\right)=\\frac{\\pi}{a^2}\\mathrm{exp}\\left(-vaz-\\frac{v^2t}{2}\\right)\\times\\sum\_{k=1}^{\\infty}kexp\\left(-\\frac{k^2\\pi^2t}{2a^2}\\right)\\mathrm{sin} \\left(k\\pi z\\right)\\ \\ 公式5

根据公式，可在漂移率v与阈值α已知的条件下计算反应时t的概率密度函数。即图1中蓝色的两个分布可整合为f(t)分布。

## 模型中各参数的意义

根据图1，对DDM模型中的各参数进行详细的解释。

漂移扩散曲线：图中那弯弯曲曲的线条表现了在选择哪种水果更好吃时内心的纠结，当线条穿过上缘(threshold)，小明终于选择了苹果(option A)。

反应时分布：图中两条蓝色的分布曲线为选择不同选项时不同反应时出现的频率，比如，上边蓝色线代表了小明每次选择苹果时纠结用时的分布，可以发现小明大多数时候的决策时间都很快，所以分布表现为正偏态。而小明选择香蕉(option B)的次数很少，所以波峰更小，但分布形式类似，说明小明对于选择水果的认知过程是相似的，只是偏好不同。注意，这两个分布不是独立的，而是从公式5中分离出来的两个分布，因此整合这两个分布可以得到公式5的分布，即实验数据中反应时的分布。

参数α—阈值(threshold)或边界(boundary)，表明了信息收集的边界，即小明心中的决策标准，当收集的信息到达这样的标准，小明就认为选择某种水果能更使自己满意。该参数可以自行设置(上一小节提到过)，也可以通过模型计算得到。例如，当小明调整自己决策的标准(阈值)时，比如香蕉要大又不能出现黑斑，此时会导致决策时间增加，而漂移率不会变化。

参数β(多数时候用z)—起始点，指决策之前的偏向，是一种先验的影响。比如，决策前小明认为香蕉更好吃(偏向β)，但是决策信息收集的途中突然想到自己已经吃了一个星期的香蕉了(dd过程)，他想换换口味，最后选择了苹果(累积信息超过边界后的决策)。

参数δ(多数时候用v)—漂移率，决定了决策的速度，受选项间主观价值差异的影响。例如，小明喜欢香蕉与苹果，而不喜欢西瓜，那么他在对香蕉与西瓜进行决策时，很容易就会选择香蕉(漂移率高)，而在对香蕉与苹果进行决策时，就可能很纠结(漂移率低)。

参数τ—非决策时间(non-decision-time)，反映了影响决策反应时中的其他因素，包括对信息编码与按键反馈的时间。可以体现个体间的决策差异，并且检验随着试次增加是否产生练习效应。

## 如何计算参数值？

(Voss et al., 2004)指出估计模型参数的问题实际就是最优化问题([机械学系中的optimization algorithm](https://zhuanlan.zhihu.com/p/22461594))，其逻辑为，实际收集数据中的反应时分布是否能被模型解释。具体来说，我们收集到的数据可以形成一个反应时分布，比如，小明在选择水果(包括苹果与香蕉)时其反应时的均值为200ms，一个标准差之内的反应时区间为\[150ms,250ms\]。而根据公式5f(t)可知，以反应时为函数的输入值也可以得到一个分布(因为f(t)是概率密度函数)，但其条件为参数v、a、z已知。因此，最优化的方法的逻辑为比较两个分布的差异，通过调整上述的参数使得两个分布差异最小。

常见的优化方法为：最大似然估计(maximum likelihood estimation, MLE)与KS检验法(Kolmogorov-Smirnov)。MLE通过比较两个分布中每一个反应时出现的概率，如公式3，求得能使两个分布中反应时出现的概率最为接近的参数，比如，实际数据中小明选择香蕉时rt=250ms的概率为0.30，而通过公式5得到的概率f(250ms|θ1)=0.25，那么可以通过改变公式中的参数获得新的概率f(250ms|θ2)=0.28去紧接真实的概率(0.30)。当然模型不止考虑某一试次的概率一致性，还应考虑整个分布概率的一致性。KS检验其实就是我们熟知的正态分布检验法，该方法不像MLE中对两个分布的单个试次进行比较，而是直接将两个分布进行比较，当两个分布的差异不显著时(α>0.05)，我们认为模型具有良好的拟合性。

(Wiecki et al., 2013)近年来越来越多的模型将分层贝叶斯(Hierarchical Bayes)的思想注入DDM中，其原因为，1.DDM受极值与缺失值的影响极大，因此需要更稳健的估计方式；2.心理学实验中的数据量可能较少(特别是神经科学领域)导致模型拟合较差，因此需要补救的算法；3.引入贝叶斯思想可以从数据中挖掘出更多的信息，比如，trial-by-trial variability、超参、参数的后验分布、更多的稳健性检验等。

分层贝叶斯思想在DDM中的实际运用体现为使用Markov chain Monte Carlo (MCMC)来估计参数的后验分布，这与以往传统算法(MLE,KS)来进行点估计是截然不同的。

先解释下贝叶斯与DDM的关系，根据公式5可知，f(t)是有关于t的条件概率分布，即在已知参数a、v、z的情况下，t=x(ms)的概率，那么根据贝叶斯定理就可以将函数f(t|a,v,z)其拆分为先验f(t)与似然f(a,v,z|t)两个部分—先验指在不知道模型参数的情况下个体主观对于t概率分布的猜测，而似然指在得到数据(t概率分布)的情况下模型参数为a、v、z的可能。其中，先验可自行设定，因此，问题的重点在于求似然，而公式5非常复杂，不能通过简单的求导计算得到最大似然，因此需要MCMC算法。

MCMC的逻辑为，当某个函数的参数已知时，通过采样的方式获取函数特征，比如，我们知道公式5是一个正态分布的概率密度函数，然而其参数众多，我们不便求得这个分布的均值与标准差，但如果我们有这个分布的样本，那么就可以通过样本来推断总体的参数。注意，正态分布有不同的表现形态，即样本与函数两种形态，通过样本求函数相对容易，而通过函数得到样本却很难，因此需要MCMC方法对函数进行采样，来获得样本，从而估计总体分布的参数。

通过结合MCMC算法，就可以计算出贝叶斯中的似然部分，从而估计出参数分布。

常见的其他概念还有吉布斯采样Gibbs sampling与超参。吉布斯采样是MCMC算法的一种形式，它的目的在于解决模型各参数之间的关联性，比如参数v时长影响参数a。吉布斯采样假设存在一个多元联合分布，所有的参数均抽取于该分布，那么对于所有参数只需在一个分布中进行抽样，而不需要分别进行抽样了，即考虑了参数间的相关性。为何要对参数进行抽样？因为前面提到，求解DDM模型参数的问题实际是最优化问题，因此需要用不同的参数来拟合模型，比较哪一组参数下的模型拟合程度最好，那么就选用哪一组参数作为模型参数，所以，吉布斯采样就是在抽取模型需要的参数，以便用于拟合模型，而采样过程中抽取的样本就形成了参数的分布情况。

超参的概念就是指，各参数分布的均值与标准差也采样于更上一层的分布。比如，计算得到的模型参数v=0.5，其参数分布为正态分布N(μ=0.5,σ=1)。超差假设，存在更高层的分布，即μ=0.5可能是从超参分布HN(0.6,2)中采样得到的，同样，σ=1也可能源自于超参分布HN(1,1)中采样得到的。参数分布与超参分布关系如图3：

![](https://pic4.zhimg.com/v2-ebd7f82648d712f996b510ace87c25cb_b.jpg)

图3 超参与参数的关系图

## trial & individual & group

在现实的数据中，我们往往只能得到被试的rt与choice，即choice表现了个体是否选择香蕉，rt反映了个体每次选择时的纠结程度。而dd过程表现的是每次选择(trial)中个体的纠结过程，但问题在于我们并不能测量出被试决策时每个试次中那如图1中纠结的曲线—即随着时间的增加V(t)的增减，因为每个trial只有一对数据，那就是rt与choice，而不是V(t)。那么，图1中的曲线是如何产生的呐？其又有何意义？

首先，在DDM的实际运用中，并不会计算V(t)，那么也不会考虑曲线是什么形态，也就是该曲线在实际应用中并没有意义。从公式5中可知，计算各参数不需要V(t)，只需要反应时分布就可以倒推出各种参数值。图1中曲线的意义在于通过图示生动形象的解释DDM的思想，另一方面其实可以通过计算出参数的DDM模型反过来去模拟每一次trial中的曲线，从而检验模型参数的可解释性(可参照建模与结果呈现部分)。

可见，DDM模型存在不同层面的定义。

在个体individual层面，个体每一次的决策拥rt与choice两个值，通过该个体各trial的数据可以计算个体层面的DDM模型参数，再通过计算出的DDM模型绘制出单个个体的evidence cumulative processing曲线，如图1中的曲线，既可以表示单个个体，也可以表示单个trial，同时也可表示一个群体group。

在群体group的层面，在求得各被试DDM的参数后，通过优化算法的方式得到group层面的DDM模型参数，同样可以根据DDM(group)去绘制群体层面的曲线图。这个地方需要注意的是：论文中的曲线图片大多时候表现得是individual层面，而论文中的表格表现得是group层面的模型参数。

很多时候，文章作者还会讨论trial层面的问题，他们认为每一次决策中的模型参数都会变化，即trial-by-trial variability，trial层面的模型参数可以与其他变量进行联合分析，比如脑影响数据、量表数据、其他实验数据。

注意：曲线图片中的x轴是反应时rt，而V(t)中的t是步数(采样率)，比如，rt=100ms，但是t=10，代表每10ms进行一次采样计算，那么会得到10次V值。这个非常容易混淆，所以有必要提出来强调一下。

总结，DDM模型的优势在于可以同时探讨多个层面的问题，此外，DDM是通过反应时分布来推断模型参数与心理过程的，因此，任何实验假设必须建立在这个最基本条件之上(Fudenberg et al., 2020)。

## DDM的发展简史

## DDM与反应时

(Ratcliff, 1978)开发了最经典的DDM模型，但当时的模型参数较少，只假设了单一的扩散过程。其最初的目的是用来拟合记忆提取过程的，该模型认为记忆是否能提取的关键在于认知中的图示是否能与现实刺激进行匹配，而匹配的过程就是漂移扩散(dd)过程，当图示与刺激存在越多共同点时，漂移率越大，记忆提取的成功率越高。由于该模型是在反应时类的心理物理实验范式上提出的，很快，该模型便被广泛用于处理反应时实验中最基础的问题—speed-accuracy trade-off(Ratcliff & McKoon, 2008)。对于speed-accuracy trade-off问题最传统的处理方式是信号检测论(signal detection theory,SDT)，可以通过ROC曲线来反映被试真实的辨别能力，也可以反映被试在实验时是否通过追求正确率而牺牲了反映速度。而DDM的优势在于，不仅能体现SDT的各种性质，还能从被试的反应中(choice&rt)中剥离出更多的成分，比如，漂移率可以反映被试的辨别能力，阈值α可以反映被试是否通过追求正确率而牺牲反映速度，此外，参数起始点z可以反映被试决策前对某个选项的偏好，非决策时间τ可以反映按键速度的个体差异。最重要的是该模型具有很好的扩展性，可以灵活的增加变动参数，从而验证各类心理理论假设。

除了DDM模型，其实还有其他很多模型也含有DDM模型类似的特征，如信息的累积，漂移率，决策条件(阈值)等。含有这些特征的模型统称为连续采样模型(Sequential sampling models SSM) ，(Ratcliff et al., 2016)对此进行了总结，如图4：

![](https://pic1.zhimg.com/v2-93a1cb707ec4d5bd59aec2571b4b06e4_b.jpg)

图4 Sequential sampling models SSM与DDM

连续采样模型Sequential samplingmodels(SSMs)已经成为对简单二元迫选决择任务的的标准，其主要特征为通过反应时来对数据进行建模。该类模型认为每个决策都是从噪音中收集有效信息形成的，即通过在一定时间内多次对累积的证据信息进行连续评估，一旦累积的证据超过某个阈值，相应的决策就会产生。该类模型对于解析潜在心理过程的视角相当引人入胜，它不仅体现了不同选项之间被选概率的差异，而且表现了不同选项反应时分布的特征。

## DDM与决策

由于DDM模型的扩展性，(Milosavljevic et al., 2010)将其引入决策领域，特别是DDM模型的内涵刚好符合以价值为基础(value-based choices)的决策理论。以价值为基础的决策理论认为，个体对于选项存在固定的偏好，比如，小明对于香蕉的偏好为V=2，而对苹果的偏好为V=1，由于偏好差异的存在，会导致小明更多并且更快的选择香蕉(Polanía et al., 2015)。而DDM的前提假设也是，个体对于选项的偏好不变，即影响个体选择的是选项间的价值差异，而不是由个体对选项主观价值的变化造成。虽然这一点仍有争议(Turner et al., 2021)，但通过DDM来探究决策机制的大门已经打开。

(Krajbich et al., 2010)将眼动技术与DDM进行结合，开发了attentional drift-diffusion model (aDDM)模型，该模型依然以价值决策理论为基础，假设具有更高主观价值的选项会获得更多的注意，而对不同选项的注意时间会影响模型的参数与个体最终的决策。比如，小明更喜欢香蕉，那么当小明把注视点移动到香蕉上时，DDM模型中的曲线向香蕉漂移(比如朝上)，而当小明看向苹果时，曲线向苹果漂移(比如朝下)，当曲线超过阈值，决策将被做出，如图5。注意，虽然曲线会受到注视点的影响，但是曲线的漂移率是固定的。

![](https://pic1.zhimg.com/v2-a21a29f3a92157ea30cedf8dd07da034_b.jpg)

图5 信息累积导致决策发生

受强化学习RL(Reinforcement learning)思想的影响，(Fontanesi et al., 2019) 等人开发出了reinforcement learning diffusion decision model (RLDDM)，其思想为，现实决策常常伴随结果反馈出现，而反馈反过来又会影响个体的决策行为。RLDDM的好处在于，一方面环缓解了基于价值决策中认为个体价值偏好不变的缺陷，另一方面可以通过DDM对强化学习过程进行更为详细的解释。更有意义的在于，RLDDM体现了DDM的扩展性，这为整合各类传统模型提供了新视野。

DDM不止能解释物理刺激对于个体的影响，(Tump et al., 2020)开发的social drift–diffusion model(sDDM)考虑了他人决策对于自我决策的影响，比如，虽然小明很喜欢吃香蕉，但是当他看见所有人都只拿苹果而不拿香蕉时，小明是否会依然选择香蕉。Tump的研究表明，当自己的决策与他人越不一致时(即与自己决策不一样的人越多)，自我的决策越容易更改，并且可以通过DDM模型中的参数漂移率进行预测。

此外，很多学者也在探究DDM模型在多元选择中的应用，以此突破DDM模型只适合二元决策的限制(Krajbich & Rangel, 2011; Roxin, 2019)，毕竟在现实生活中，人们面临的决策问题通常不止有两个备选项。

## 模型在计算上的发展

在前面的模型推导过程中，我们介绍了标准DDM的参数推导过程，包括参数漂移率v、上边界a(下边界为0)、初始值z(不设置时为a/2)。而现阶段被实际应用的DDM模型已经有了非常多的变化。

(Ratcliff & Tuerlinckx, 2002)提出了非决策反应时non-decision-time的概念，意图在于把模型中的反应时变量rt分解为与决策有关的反应时t与决策无关的非决策反应时间t0，即t0=rt-t，这样有利于避免由于实验设备等因素造成的影响。非决策反应时t0包括，对刺激的编码、按键反应与表征转化的用时(Ratcliff et al., 2016)。

试次间的参数差异trial by trial variability，也可表示为across-trial variability，指在每一次不同的决策中，模型的参数也可能不相同，比如，由于每一次决策时刺激间的差异不同，导致模型漂移率发生变化(Ratcliff et al., 2016)。其假设为，即使物理刺激条件是相同的，但与决策相关的信息的内部表征却不相同。分析试次间的参数差异可以了解被试在实验中的变化，也可以更好的对比个体差异，更重要的意义在于利用各个试次的参数与脑神经数据进行回归分析，从而了解模型理论、心理机制与脑机制解释的一致性。其中，常见的扩展模型的方式为引入softmax函数，即假设模型参数与脑神经数据之间的关系为非线性关系(Baldassi et al., 2020)。

自从HDDM(hierarchical drift diffusion model)提出以来(Wiecki et al., 2013)，近年有关DDM模型的文章几乎都用此方法进行模型的参数估计。前面我们已经解释了该方法中参数估计的基本原理，需要强调的是，HDDM只是在模型参数估计的方法上有所不同，而不像其他一些DDM扩展模型会改变参数的定义，比如后面提到的aDDM、RLDDM、sDDM都可以使用HDDM的逻辑进行参数估计。

aDDM(attentional drift-diffusion model)的目的在于考察眼动对于决策的影响，因此，该模型根据决策时注视点的位置把反应时rt分为不同阶段，如图：

$V_t=V_{t-1}+d\left(r_{left}-\theta r_{right}\right)+\varepsilon_t\ \ \ \ \ \ \ \ \ 公式6$V\_t=V\_{t-1}+d\\left(r\_{left}-\\theta r\_{right}\\right)+\\varepsilon\_t\\ \\ \\ \\ \\ \\ \\ \\ \\ 公式6

从公式6中可见，aDDM模型中注视点的转移影响的参数为漂移率，其中d与θ为常数，r为对选项的主观价值，rleft即对左边选项的主观价值感，rright为对右边选项的主观价值感。在每个试次中，当注视点为左边选项时，公式为rleft-rright，而当注视点为右边选项时，公式变为rright-rleft。其中，d越大说明漂移率对dd过程的影响越大，θ为0~1之间的数，θ越大说明注视的影响越小。

RLDDM(reinforcement learning diffusion decision model)的目的在于整合RL模型来解释反馈对于决策的影响。

$Q_t=Q_{t-1}+\eta·ft-Qt-1       公式7$Q\_t=Q\_{t-1}+\\eta·ft-Qt-1 公式7

公式7为强化学习模型RL的原理，即对选项的主观价值Q受到之前对该选项的主观价值与当前刺激反馈的影响。其中ft为当前刺激反馈的强度，ft越大说明刺激反馈的程度越超过自我对选项的预期，导致当前对选项的主观价值判断变化越大。η是学习率，可以控制ft的影响。

$v_t=\gamma\left(Q_{A,t}-Q_{B,t}\right)\ \ \ \ \ \ \ \ \ \ 公式8$v\_t=\\gamma\\left(Q\_{A,t}-Q\_{B,t}\\right)\\ \\ \\ \\ \\ \\ \\ \\ \\ \\ 公式8

通过公式8可见，RL模型中选项主观价值对漂移率的影响。其中，QAt为对选项A的主观价值偏好，QBt为对选项B的主观价值偏好，γ可以控制主观价值对漂移率影响的大小。需要注意的是，漂移率在每个试次都不同，因此该模型考虑了trial by trial variability。除此之外，RL模型中的主观价值还可以对DDM模型中的其他参数造成影响，因此，模型如何搭建主要依赖于理论框架的设定，这也体现了DDM的灵活性。

sDDM(social drift–diffusion model)的目的在于体现社会决策中他人决策行为的影响。

$V_t=V_{t-1}+\left(v_p+v_{s,t}\right)+\varepsilon_t\ \ \ \ \ 公式9$V\_t=V\_{t-1}+\\left(v\_p+v\_{s,t}\\right)+\\varepsilon\_t\\ \\ \\ \\ \\ 公式9

公式9中，vp代表自我对于选项的倾向性，vst代表他人决策对自我决策的影响，并且该影响随着试次变化。vp+vst共同构成了总的漂移率v。因此，该模型的理论假设也是认为，他人决策影响的是模型的漂移率，即个体对于选项的辨别能力。

综上所述，DDM模型可用于各种决策场景，体现了其丰富的扩展性，并随着算法的进步，其参数拟合的效率也在提升。

## 建模与结果呈现

DDM模型是通过反应时rt与决策行为choice为基础，其基本的数据结果如图6(Wiecki et al., 2013)。

![](https://pic2.zhimg.com/v2-5aa7f099104e5204779ee06ca5046c19_b.jpg)

图6 示例数据结构

虽然拟合模型存在不同的方式，当数据结果基本相同，必须包含的字段为被试编号subj\_idx，反应时rt，决策行为response，如果存在不同的实验条件cond也可以选择性加入。

常见模型拟合的方式有：(Wiecki et al., 2013)提供的python包hddm；(Shinn et al., 2020)提供的python包pyddm，(Wabersich & Vandekerckhove, 2014)提供的JAGS with the Wiener module extension(可结合R语言中的rjags包一起使用，也可以结合python中的pystan包使用)；国内张磊大神等开发的R包hbayesDM(Ahn et al., 2017)。

本文以python中HDDM包为例，展现如何进行DDM建模以及相应的结果呈现(Wiecki et al., 2013)。更多信息请参考[http://ski.clps.brown.edu/hddm\_docs/tutorial\_python.html](https://link.zhihu.com/?target=http%3A//ski.clps.brown.edu/hddm_docs/tutorial_python.html)。

提示：在进行数学建模以前，请查看数据中是否错在缺失值与异常数据。在做DDM模型前一般会进行线性模型类的分析，本文将跳过这些步骤，直接讲解如何进行DDM建模。

```
1.import matplotlib.pyplot as plt #导入绘图包  
2.import hddm #导入hddm模型包  
3.  
4.data = hddm.load_csv('data.csv') # 导入数据，注意，请放在工作目录下，最好使用csv文件，csv文件中包含header  
5.data.head(10)# 显示数据
```

![](https://pic2.zhimg.com/v2-8a94504455646effcadc3b0c8e3a680d_b.jpg)

```
6.data = hddm.utils.flip_errors(data)# 使错误选项response=0的rt为负  
7.# subj_idx是被试编号  
8.# stim是实验条件，包括LL,WL,WW三种  
9.# conf是对实验条件的分类，LL与WW为LC，WL为HC  
10.# dbs(deep brain stimulation)为是否是脑损伤患者:1为是 0为不是  
11.# theta为EEG数据  
12.  
13.m = hddm.HDDM(data) # 模型设定，可以在此部分设定实验条件  
14.m.find_starting_values() # 设定初始参数  
15.m.sample(2000, burn=20) # 开始进行MCMC参数估计  
16.  
17.m.gen_stats()[stats.index.isin(['a', 'a_std', 'a_subj.0', 'a_subj.1'])]# 显示模型参数
```

![](https://pic4.zhimg.com/v2-bb7a41397df98ac2b0d7ae2eb18474e3_b.jpg)

```
18.# 其中a(阈值)代表group层面的模型参数；a_std是a的标准差；a_subj.x可以显示individual层面的模型参数。  
19.# 这里只演示了阈值相关的参数信息，其他参数可自行查看，如'v'为漂移率，'z'为起始点，'t'为非决策时间。  

1.# 绘图  
2.m.plot_posteriors(['a', 't', 'v', 'a_std']) # 绘制各参数的后验分布。
```

![](https://pic4.zhimg.com/v2-bb3b15beca317cfbe143ee864d7ba937_b.jpg)

```
3.# 其中trace图展现了随着抽样的进行，参数的变化情况；  
4.# acorr为自相关图，表达了随着抽样的进行，参数的是否稳定，因为参数可能随着抽样越来越大，而不是趋于一个稳定值。  
5.# trace与acorr图有助于判断，模型参数是否收敛，图例中的参数是收敛的。  
6.# 柱状图为参数分布情况，主要看这个就可以了。  
7.  
8.# Gelman-Rubin方法提供了更正式的模型收敛检验法  
9.models = []  
10.for i in range(5):  
11.    m = hddm.HDDM(data)  
12.    m.find_starting_values()  
13.    m.sample(5000, burn=20)  
14.    models.append(m)  
15.hddm.analyze.gelman_rubin(models)  
16.# 此方法非常耗时，显示的结果为所有参数的标准差(变异)，若所有值都接近1，说明模型收敛。  
```

![](https://pic1.zhimg.com/v2-96ff1f0421be3be92399e9f58eb36834_b.jpg)

```
17.  
18.m.plot_posterior_predictive(figsize=(14, 10))# 将数据分布与模型分布进行对比，检测模型的拟合程度  

1.# 红线为实际数据，蓝线为模型拟合数据。共14副图，表示14名被试。  
2.  
3.# 带实验条件的模型分析 + 对参数的假设检验  
4.m_stim = hddm.HDDM(data, depends_on={'v': 'stim'})# 计算不同条件下的模型参数  
5.# 本例子中认为，实验条件(stim)只影响模型参数漂移率v。  
6.# 可根据自己的理论假设来设定条件与参数的关系，比如设定阈值参数受刺激条件的影响，'a': 'stim'。  
7.m_stim.find_starting_values()  
8.m_stim.sample(10000, burn=1000)# 进行计算分析，不在赘述  
9.# 绘制不同条件下的参数分布  
10.v_WW, v_LL, v_WL = m_stim.nodes_db.node[['v(WW)', 'v(LL)', 'v(WL)']]# 提取参数v 括号中为刺激条件stim:WW LL WL  
11.hddm.analyze.plot_posterior_nodes([v_WW, v_LL, v_WL])# 进行绘图 
```

![](https://pic1.zhimg.com/v2-9915d4c2f28682f929e0da7572af74c8_b.jpg)

```
12.# 从图中可见，WL条件下的漂移率v显著大于其他两个条件  
13.(v_LL.trace() > v_WL.trace()).mean() # 进行显著性检验  
14.# p=0.00011, 说明LL与WL条件下的漂移率V存在显著差异  
15.  
16.# 模型拟合度比较  
17.m.dic # 无刺激条件模型m的DIC(deviance information criterion)拟合度指标  
18.m_stim.dic # 刺激条件下模型m_stim的DIC拟合度指标  
19.# m model DIC: 10960.88  
20.# m_stim model DIC: 10774.75  
21.# DIC越小说明模型拟合度越好，所以，m_stim model模型拟合性更好  
22.  
23.# 拟合HDDM回归模型  
24.# 目的在于，结合模型参数与脑神经数据  
25.m_reg = hddm.HDDMRegressor(data[data.dbs == 0],  
26.                           "a ~ theta:C(conf, Treatment('LC'))",  
27.                           depends_on={'v': 'stim'})  
28.# HDDMRegressor为建立模型，data部分选择非脑损伤(dbs=0)被试  
```

## 总结

本文回顾了DDM模型的发展历程，对其公式进行了推导，简述了DDM模型与价值决策的关系，并对如何建模进行了演示。

## 参考文献

Ahn, W.-Y., Haines, N., & Zhang, L. (2017). Revealing Neurocomputational Mechanisms of Reinforcement Learning and Decision-Making With the hBayesDM Package. _Computational Psychiatry_, _1_(0), 24. [https://doi.org/10.1162/cpsy\_a\_00002](https://link.zhihu.com/?target=https%3A//doi.org/10.1162/cpsy_a_00002)

Baldassi, C., Cerreia-Vioglio, S., Maccheroni, F., Marinacci, M., & Pirazzini, M. (2020). A Behavioral Characterization of the Drift Diffusion Model and Its Multialternative Extension for Choice Under Time Pressure. _Management Science_, _66_(11), 5075–5093. [https://doi.org/10.1287/mnsc.2019.3475](https://link.zhihu.com/?target=https%3A//doi.org/10.1287/mnsc.2019.3475)

Conitzer, V., Sinnott-Armstrong, W., Borg, J. S., Deng, Y., & Kramer, M. (2017). Moral decision making frameworks for artificial intelligence. _AAAI Workshop - Technical Report_, _WS_\-_17_\-_01_\-(Moor 2006), 105–109.

Cruwys, T., Greenaway, K. H., Ferris, L. J., Rathbone, J. A., Saeri, A. K., Williams, E., Parker, S. L., Chang, M. X. L., Croft, N., Bingley, W., & Grace, L. (2021). When trust goes wrong: A social identity model of risk taking. _Journal of Personality and Social Psychology_, _120_(1), 57–83. [https://doi.org/10.1037/pspi0000243](https://link.zhihu.com/?target=https%3A//doi.org/10.1037/pspi0000243)

Evans, J. S. B. T. (2008). Dual-processing accounts of reasoning, judgment, and social cognition. _Annual Review of Psychology_, _59_(1), 255–278. [https://doi.org/10.1146/annurev.psych.59.103006.093629](https://link.zhihu.com/?target=https%3A//doi.org/10.1146/annurev.psych.59.103006.093629)

Feller, W. (1968). An Introduction to Probability Theory and its Applications: Volume 1. In _New York, NY: Wiley_ (Vol. 1, Issue 3rd Edn). [https://philpapers.org/rec/FELAIT-4](https://link.zhihu.com/?target=https%3A//philpapers.org/rec/FELAIT-4)

Fischhoff, B., & Broomell, S. B. (2020). Judgment and Decision Making. _Annual Review of Psychology_, _71_(1), 331–355. [https://doi.org/10.1146/annurev\-psych-010419-050747](https://link.zhihu.com/?target=https%3A//doi.org/10.1146/annurev-psych-010419-050747)

Fontanesi, L., Gluth, S., Spektor, M. S., & Rieskamp, J. (2019). A reinforcement learning diffusion decision model for value-based decisions. _Psychonomic Bulletin & Review_, _26_(4), 1099–1121. [https://doi.org/10.3758/s13423-018-1554-2](https://link.zhihu.com/?target=https%3A//doi.org/10.3758/s13423-018-1554-2)

Fudenberg, D., Newey, W., Strack, P., & Strzalecki, T. (2020). Testing the drift-diffusion model. _Proceedings of the National Academy of Sciences_, _117_(52), 33141–33148. [https://doi.org/10.1073/pnas.2011446117](https://link.zhihu.com/?target=https%3A//doi.org/10.1073/pnas.2011446117)

Johnson, D. J., Hopwood, C. J., Cesario, J., & Pleskac, T. J. (2017). Advancing Research on Cognitive Processes in Social and Personality Psychology: A Hierarchical Drift Diffusion Model Primer. _Social Psychological and Personality Science_, _8_(4), 413–423. [https://doi.org/10.1177/1948550617703174](https://link.zhihu.com/?target=https%3A//doi.org/10.1177/1948550617703174)

Krajbich, I., Armel, C., & Rangel, A. (2010). Visual fixations and the computation and comparison of value in simple choice. _Nature Neuroscience_, _13_(10), 1292–1298. [https://doi.org/10.1038/nn.2635](https://link.zhihu.com/?target=https%3A//doi.org/10.1038/nn.2635)

Krajbich, I., & Rangel, A. (2011). Multialternative drift-diffusion model predicts the relationship between visual fixations and choice in value-based decisions. _Proceedings of the National Academy of Sciences of the United States of America_, _108_(33), 13852–13857. [https://doi.org/10.1073/pnas.1101328108](https://link.zhihu.com/?target=https%3A//doi.org/10.1073/pnas.1101328108)

Miletić, S., Boag, R. J., Trutti, A. C., Stevenson, N., Forstmann, B. U., & Heathcote, A. (2021). A new model of decision processing in instrumental learning tasks. _ELife_, _10_, 1–55. [https://doi.org/10.7554/eLife.63055](https://link.zhihu.com/?target=https%3A//doi.org/10.7554/eLife.63055)

Milosavljevic, M., Malmaud, J., Huth, A., Koch, C., & Rangel, A. (2010). The drift diffusion model can account for value-based choice response times under high and low time pressure. _Judgement & Decision Making_, _5_(6), 437–449. [https://www.researchgate.net/profile/Alexander\_Huth/publication/47630977\_The\_Drift\_Diffusion\_Model\_Can\_Account\_for\_the\_Accuracy\_and\_Reaction\_Time\_of\_Value-Based\_Choices\_Under\_High\_and\_Low\_Time\_Pressure/links/0046352f10dfd424ce000000.pdf](https://link.zhihu.com/?target=https%3A//www.researchgate.net/profile/Alexander_Huth/publication/47630977_The_Drift_Diffusion_Model_Can_Account_for_the_Accuracy_and_Reaction_Time_of_Value-Based_Choices_Under_High_and_Low_Time_Pressure/links/0046352f10dfd424ce000000.pdf)

Polanía, R., Moisa, M., Opitz, A., Grueschow, M., & Ruff, C. C. (2015). The precision of value-based choices depends causally on fronto-parietal phase coupling. _Nature Communications_, _6_. [https://doi.org/10.1038/ncomms9090](https://link.zhihu.com/?target=https%3A//doi.org/10.1038/ncomms9090)

Ratcliff, R. (1978). A theory of memory retrieval. _Psychological Review_, _85_(2), 59–108. [https://doi.org/10.1037/0033-295X.85.2.59](https://link.zhihu.com/?target=https%3A//doi.org/10.1037/0033-295X.85.2.59)

Ratcliff, R., & McKoon, G. (2008). The diffusion decision model: theory and data for two-choice decision tasks. _Neural Computation_, _20_(4), 873–922. [https://doi.org/10.1162/neco.2008.12-06-420](https://link.zhihu.com/?target=https%3A//doi.org/10.1162/neco.2008.12-06-420)

Ratcliff, R., Smith, P. L., Brown, S. D., & McKoon, G. (2016). Diffusion Decision Model: Current Issues and History. _Trends in Cognitive Sciences_, _20_(4), 260–281. [https://doi.org/10.1016/j.tics.2016.01.007](https://link.zhihu.com/?target=https%3A//doi.org/10.1016/j.tics.2016.01.007)

Ratcliff, R., & Tuerlinckx, F. (2002). Estimating parameters of the diffusion model: Approaches to dealing with contaminant reaction times and parameter variability. _Psychonomic Bulletin and Review_, _9_(3), 438–481. [https://doi.org/10.3758/BF03196302](https://link.zhihu.com/?target=https%3A//doi.org/10.3758/BF03196302)

Roxin, A. (2019). Drift–diffusion models for multiple-alternative forced-choice decision making. _Journal of Mathematical Neuroscience_, _9_(1). [https://doi.org/10.1186/s13408-019-0073-4](https://link.zhihu.com/?target=https%3A//doi.org/10.1186/s13408-019-0073-4)

Shinn, M., Lam, N. H., & Murray, J. D. (2020). A flexible framework for simulating and fitting generalized drift-diffusion models. _ELife_, _9_, 1–27. [https://doi.org/10.7554/ELIFE.56938](https://link.zhihu.com/?target=https%3A//doi.org/10.7554/ELIFE.56938)

Tump, A. N., Pleskac, T. J., & Kurvers, R. H. J. M. (2020). Wise or mad crowds? The cognitive mechanisms underlying information cascades. _Science Advances_, _6_(29), eabb0266. [https://doi.org/10.1126/sciadv.abb0266](https://link.zhihu.com/?target=https%3A//doi.org/10.1126/sciadv.abb0266)

Turner, W., Feuerriegel, D., Andrejević, M., Hester, R., & Bode, S. (2021). Perceptual change-of-mind decisions are sensitive to absolute evidence magnitude. _Cognitive Psychology_, _124_, 101358. [https://doi.org/10.1016/j.cogpsych.2020.101358](https://link.zhihu.com/?target=https%3A//doi.org/10.1016/j.cogpsych.2020.101358)

Voss, A., Rothermund, K., & Voss, J. (2004). Interpreting the parameters of the diffusion model: An empirical validation. _Memory and Cognition_, _32_(7), 1206–1220. [https://doi.org/10.3758/BF03196893](https://link.zhihu.com/?target=https%3A//doi.org/10.3758/BF03196893)

Wabersich, D., & Vandekerckhove, J. (2014). Extending JAGS: A tutorial on adding custom distributions to JAGS (with a diffusion model example). _Behavior Research Methods_, _46_(1), 15–28. [https://doi.org/10.3758/s13428-013-0369-3](https://link.zhihu.com/?target=https%3A//doi.org/10.3758/s13428-013-0369-3)

Wiecki, T. V., Sofer, I., & Frank, M. J. (2013). HDDM: Hierarchical Bayesian estimation of the Drift-Diffusion Model in Python. _Frontiers in Neuroinformatics_, _7_(JULY 2013), 1–10. [https://doi.org/10.3389/fninf.2013.00014](https://link.zhihu.com/?target=https%3A//doi.org/10.3389/fninf.2013.00014)

Zhang, L., & Gläscher, J. (2020). A brain network supporting social influences in human decision-making. _Science Advances_, _6_(34), eabb4159. [https://doi.org/10.1126/sciadv.abb4159](https://link.zhihu.com/?target=https%3A//doi.org/10.1126/sciadv.abb4159)