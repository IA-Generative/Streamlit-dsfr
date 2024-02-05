<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue'
import { Streamlit } from '~/stcomponentlib'
import { DsfrButtonGroup } from '@gouvminint/vue-dsfr'

import { useStreamlit } from '~/streamlit'
import type { ComponentProps } from '~/types/ComponentProps.d.ts'
import DsfrButton from '~/components/dsfr/DsfrButton.vue'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		align?: 'left' | 'center' | 'right'
		inlineLayoutWhen?: 'never' | 'always' | 'small' | 'medium' | 'large'
		reverse?: boolean
		iconRight?: boolean
		size?: 'small' | 'medium' | 'large'
		buttons?: {
			label?: string
			secondary?: boolean
			tertiary?: boolean
			disabled?: boolean
			icon?: string
			iconOnly?: boolean
			noOutline?: boolean
			// Omitted: iconRight, size
			// Custom props
			link?: string
			copy?: string
		}[]
		equisized?: boolean
	}>
>()

const clicked = ref<boolean[]>(Array(props.args.buttons?.length ?? 0).fill(false))

function onRenderEvent(_event: Event): void
{
	if (clicked.value.some(value => value))
	{
		clicked.value = Array(props.args.buttons?.length ?? 0).fill(false)
		Streamlit.setComponentValue([...clicked.value])
	}
}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

async function onClickIndex(index: number): Promise<void>
{
	if (clicked.value.some(value => value))
	{
		clicked.value = Array(props.args.buttons?.length ?? 0).fill(false)
		Streamlit.setComponentValue([...clicked.value])

		await new Promise(resolve => setTimeout(resolve, 50))
	}

	clicked.value[index] = true
	Streamlit.setComponentValue([...clicked.value])
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButtonGroup
			v-bind="props.args"
			:buttons="undefined"
			:disabled="props.disabled"
		>
			<li
				v-for="(button, i) in (props.args.buttons || [])"
				:key="i"
			>
				<DsfrButton
					v-bind="button"
					:disabled="clicked[i] || props.disabled || button.disabled"
					@click="() => onClickIndex(i)"
				/>
			</li>
		</DsfrButtonGroup>
	</div>
</template>

<style scoped>
.component {
	/* Ensure consistent height */
	overflow: hidden;
}
.component :deep(.fr-btns-group) {
	/* Remove the bottom margin of the button group */
	margin-bottom: -1rem;
}
</style>
